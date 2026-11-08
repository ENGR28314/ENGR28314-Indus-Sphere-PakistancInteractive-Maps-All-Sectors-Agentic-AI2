"""CRS-aware DEM reservoir storage/elevation analysis for IndusSphere Pakistan.

The uploaded reservoir maximum-pool boundary is assumed to be GeoJSON in
WGS 84 longitude/latitude (EPSG:4326), as required by RFC 7946. DEMs must carry
valid CRS metadata. The DEM is warped once to a selected metric WGS 84 / UTM CRS;
the boundary is transformed with always_xy=True and rasterized on that exact
output grid to avoid independent-grid alignment drift.
"""
from __future__ import annotations

import json
from typing import Any

import numpy as np
import pandas as pd


PAKISTAN_UTM = {
    "WGS 84 / UTM zone 41N — western Pakistan (60°E–66°E)": 32641,
    "WGS 84 / UTM zone 42N — central/western Pakistan (66°E–72°E)": 32642,
    "WGS 84 / UTM zone 43N — eastern/northern Pakistan (72°E–78°E)": 32643,
}


def utm_epsg_for_lon(longitude: float) -> int:
    """Return WGS84 UTM north EPSG code for a longitude in Pakistan's span."""
    if not -180 <= longitude <= 180:
        raise ValueError("Longitude must be between -180 and 180 degrees")
    zone = int((longitude + 180) // 6) + 1
    if zone not in (41, 42, 43):
        raise ValueError("Longitude is outside Pakistan's UTM zones 41N–43N")
    return 32600 + zone


def storage_curve_from_array(elevations_m, pixel_area_m2: float, level_step_m: float = 1.0) -> pd.DataFrame:
    """Compute area and volume for a clipped reservoir-basin elevation array."""
    z = np.asarray(elevations_m, dtype="float64")
    z = z[np.isfinite(z)]
    if z.size == 0:
        raise ValueError("No valid DEM elevation pixels fall inside the reservoir boundary")
    if pixel_area_m2 <= 0 or level_step_m <= 0:
        raise ValueError("Pixel area and water-level interval must be positive")
    lo = float(np.floor(np.nanmin(z)))
    hi = float(np.ceil(np.nanmax(z)))
    if hi <= lo:
        hi = lo + level_step_m
    levels = np.arange(lo, hi + level_step_m * 0.5, level_step_m)
    rows = []
    for level in levels:
        depth = np.maximum(level - z, 0.0)
        wet = depth > 0
        area = float(np.count_nonzero(wet) * pixel_area_m2)
        volume = float(np.sum(depth) * pixel_area_m2)
        rows.append({"water_level_m": float(level), "water_surface_area_m2": area,
                     "water_surface_area_ha": area / 10000.0,
                     "storage_m3": volume, "storage_Mm3": volume / 1_000_000.0,
                     "storage_acre_ft": volume / 1233.48184})
    return pd.DataFrame(rows)


def _geojson_geometry(geojson_bytes: bytes):
    from shapely.geometry import shape
    payload = json.loads(geojson_bytes.decode("utf-8"))
    kind = payload.get("type")
    if kind == "FeatureCollection":
        geoms = [shape(f["geometry"]) for f in payload.get("features", []) if f.get("geometry")]
        if not geoms:
            raise ValueError("GeoJSON FeatureCollection contains no geometries")
        from shapely.ops import unary_union
        geom = unary_union(geoms)
    elif kind == "Feature":
        geom = shape(payload["geometry"])
    else:
        geom = shape(payload)
    if geom.is_empty or not geom.is_valid:
        raise ValueError("Reservoir boundary is empty or invalid; repair the GeoJSON geometry")
    if geom.geom_type not in ("Polygon", "MultiPolygon"):
        raise ValueError("Upload a Polygon or MultiPolygon reservoir boundary")
    return geom


def compute_dem_storage_curve(dem_bytes: bytes, boundary_geojson: bytes,
                              target_epsg: int, level_step_m: float = 1.0) -> dict[str, Any]:
    """Warp DEM to metric UTM, rasterize boundary on same grid, and compute curve."""
    try:
        import rasterio
        from rasterio.io import MemoryFile
        from rasterio.warp import calculate_default_transform, reproject, Resampling
        from rasterio.features import geometry_mask
        from pyproj import CRS, Transformer
        from shapely.ops import transform as shapely_transform
    except ImportError as exc:
        raise RuntimeError("DEM processing dependencies are missing. Install rasterio and pyproj.") from exc

    if target_epsg not in (32641, 32642, 32643):
        raise ValueError("Select a Pakistan WGS 84 / UTM CRS: EPSG:32641, 32642 or 32643")
    boundary_wgs84 = _geojson_geometry(boundary_geojson)
    target_crs = CRS.from_epsg(target_epsg)
    to_target = Transformer.from_crs("EPSG:4326", target_crs, always_xy=True)
    boundary_projected = shapely_transform(to_target.transform, boundary_wgs84)

    with MemoryFile(dem_bytes) as memfile:
        with memfile.open() as src:
            if src.crs is None:
                raise ValueError("DEM has no CRS metadata. Assign the correct source CRS before analysis; do not guess it.")
            if src.count < 1:
                raise ValueError("DEM contains no raster bands")
            source_crs_obj = CRS.from_user_input(src.crs)
            if not source_crs_obj.is_projected and source_crs_obj.to_epsg() is None:
                raise ValueError("DEM source CRS could not be interpreted. Verify its CRS metadata before processing.")
            target_axes = target_crs.axis_info
            if len(target_axes) < 2 or any(abs(float(ax.unit_conversion_factor or 0) - 1.0) > 1e-9 for ax in target_axes[:2]):
                raise ValueError("Selected analysis CRS must use metres on both horizontal axes.")
            transform, width, height = calculate_default_transform(
                src.crs, target_crs, src.width, src.height, *src.bounds
            )
            if width * height > 50_000_000:
                raise ValueError("Reprojected DEM exceeds 50 million cells. Clip/resample the DEM to the reservoir study area first.")
            dst = np.full((height, width), np.nan, dtype="float32")
            reproject(
                source=rasterio.band(src, 1), destination=dst,
                src_transform=src.transform, src_crs=src.crs,
                src_nodata=src.nodata, dst_transform=transform,
                dst_crs=target_crs, dst_nodata=np.nan,
                resampling=Resampling.bilinear,
            )
            # Explicit overlap check before rasterization: catches wrong CRS,
            # wrong datum assignment and boundaries outside the DEM footprint.
            from rasterio.transform import array_bounds
            left, bottom, right, top = array_bounds(height, width, transform)
            dem_footprint = __import__("shapely.geometry", fromlist=["box"]).box(left, bottom, right, top)
            if not boundary_projected.intersects(dem_footprint):
                raise ValueError("Reservoir boundary does not overlap the reprojected DEM. Check source CRS, GeoJSON EPSG:4326 coordinates, datum transformation and study-area extent.")
            inside = geometry_mask([boundary_projected.__geo_interface__],
                                   out_shape=(height, width), transform=transform,
                                   invert=True, all_touched=False)
            valid = inside & np.isfinite(dst)
            if not np.any(valid):
                raise ValueError("No valid DEM cells intersect the reservoir boundary. Check coordinate reference systems, boundary location and DEM NoData coverage.")
            if src.nodata is not None:
                # Reproject has already mapped declared NoData to NaN.
                pass
            clipped = np.where(valid, dst, np.nan)
            pixel_area = abs(transform.a * transform.e - transform.b * transform.d)
            curve = storage_curve_from_array(clipped, pixel_area, level_step_m)
            source_crs = src.crs.to_string()
            source_bounds = tuple(float(v) for v in src.bounds)
            source_resolution = tuple(float(v) for v in src.res)
            source_nodata = src.nodata
            source_shape = (src.height, src.width)
            analysis_transform = tuple(float(v) for v in transform)
            analysis_bounds = tuple(float(v) for v in (left, bottom, right, top))
            analysis_resolution = (float(np.hypot(transform.a, transform.d)),
                                   float(np.hypot(transform.b, transform.e)))
            boundary_area_m2 = float(boundary_projected.area)
            rasterized_area_m2 = float(np.count_nonzero(inside) * pixel_area)
            valid_area_m2 = float(np.count_nonzero(valid) * pixel_area)

    # Approximate longitude of boundary centroid is sufficient for zone advisory only.
    centroid_lon = float(boundary_wgs84.centroid.x)
    suggested_epsg = utm_epsg_for_lon(centroid_lon)
    return {
        "curve": curve,
        "metadata": {
            "source_dem_crs": source_crs,
            "analysis_crs": f"EPSG:{target_epsg}",
            "suggested_utm_epsg_from_boundary_centroid": suggested_epsg,
            "source_dem_shape": f"{source_shape[1]} × {source_shape[0]} pixels",
            "source_dem_bounds": source_bounds,
            "source_dem_resolution": source_resolution,
            "source_nodata": source_nodata,
            "analysis_grid_shape": f"{width} × {height} pixels",
            "analysis_pixel_area_m2": float(pixel_area),
            "analysis_pixel_size_m": analysis_resolution,
            "analysis_affine_transform": analysis_transform,
            "analysis_grid_bounds_m": analysis_bounds,
            "projected_boundary_area_m2": boundary_area_m2,
            "rasterized_boundary_area_m2": rasterized_area_m2,
            "valid_dem_area_m2": valid_area_m2,
            "valid_dem_coverage_pct_of_rasterized_boundary": (100.0 * valid_area_m2 / rasterized_area_m2) if rasterized_area_m2 else 0.0,
            "valid_dem_pixels_in_boundary": int(np.count_nonzero(valid)),
            "boundary_input_crs_assumption": "EPSG:4326 (RFC 7946 GeoJSON longitude/latitude)",
            "method": "Single DEM warp to metric UTM; boundary transformed with always_xy; polygon rasterized on identical output affine grid; pixel-summed water depth volume.",
        },
    }
