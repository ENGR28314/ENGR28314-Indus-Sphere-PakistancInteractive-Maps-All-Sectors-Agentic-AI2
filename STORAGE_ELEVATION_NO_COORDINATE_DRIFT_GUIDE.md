# Extracting Storage-Elevation Curves Without Coordinate Drift

## Purpose

This workflow derives an indicative reservoir elevation-area-capacity relationship from a terrain DEM and a reservoir-basin polygon. It is designed to prevent horizontal coordinate misalignment between the raster and vector inputs.

## Required inputs

1. **DEM GeoTIFF** with a correct source CRS, affine transform, NoData value, and horizontal units. The elevation band must be in metres for the current calculation. Record the vertical datum (for example, the project's surveyed vertical datum/geoid realization) separately; horizontal EPSG metadata does not establish the vertical datum.
2. **Reservoir basin boundary** as RFC 7946 GeoJSON, whose coordinates are longitude then latitude in WGS 84 (EPSG:4326). If the boundary comes from a projected shapefile or CAD survey, transform it to EPSG:4326 using its actual source CRS and a documented datum operation before exporting GeoJSON.
3. **Local analysis CRS** selected from WGS 84 / UTM 41N (EPSG:32641), 42N (EPSG:32642), or 43N (EPSG:32643), according to the reservoir location.

## Coordinate-drift prevention sequence

1. Inspect the DEM's declared CRS, geotransform, pixel size, bounds and NoData value. Never assign a CRS merely to make a layer appear in the correct place.
2. Confirm the boundary coordinates are GeoJSON longitude/latitude. Do not pass projected eastings/northings into a GeoJSON upload.
3. Transform the boundary from EPSG:4326 to the selected UTM CRS with explicit X/Y axis order (`always_xy=True`).
4. Reproject the DEM once to a single target raster grid. Preserve the resulting affine transform, dimensions and bounds.
5. Rasterize the transformed polygon using that exact affine transform and the exact output width/height. Do not create a second independently aligned raster and compare array indices.
6. Check that the projected polygon intersects the DEM footprint and that valid DEM pixels exist inside it.
7. Review the reported grid transform, pixel size, bounds, pixel area, rasterized boundary area and valid-data coverage. Compare independent survey control points and known reservoir levels before engineering use.

## Capacity calculation

For each trial water-surface elevation `H`, terrain elevation at cell `i` is `z_i`, and projected cell area is `A`:

- Water depth: `d_i = max(H - z_i, 0)`
- Water-surface area: `Area(H) = count(d_i > 0) × A`
- Storage: `V(H) = Σ d_i × A`

Conversions used by the application:

- hectares = square metres / 10,000
- million cubic metres = cubic metres / 1,000,000
- acre-feet = cubic metres / 1,233.48184

## Quality-control interpretation

- A boundary/DEM non-overlap error usually indicates an incorrect source CRS, incorrect GeoJSON coordinates, an unhandled datum transformation, or the wrong study-area extent.
- Low valid-data coverage indicates NoData gaps or incomplete DEM coverage; do not treat missing cells as zero elevation.
- A UTM zone mismatch warning requires review of the reservoir longitude and whether the project crosses a zone boundary. For large or multi-zone basins, select an appropriate regional projected CRS after geodetic review rather than forcing one UTM zone.
- Horizontal coordinate alignment does not correct vertical-datum offsets. DEM elevations and reservoir gauge/survey elevations must share a verified vertical reference before comparison.
- Pixel-summed volume is an approximation. DEM resolution, interpolation, vegetation/buildings, shoreline representation, bathymetry below water level and rasterization rules all affect the result.

## Limitations

This method estimates topographic storage from the supplied terrain surface and boundary. It does not replace a bathymetric survey, official elevation-area-capacity table, sedimentation assessment, dead-storage determination, operational rule curve, spillway/outlet analysis, or dam-safety study. Use verified WAPDA / provincial irrigation / project survey data for official capacities and operational decisions.
