import numpy as np
import pytest
from reservoir_dem_gis import utm_epsg_for_lon, storage_curve_from_array


def test_pakistan_utm_zone_codes():
    assert utm_epsg_for_lon(64.0) == 32641
    assert utm_epsg_for_lon(69.0) == 32642
    assert utm_epsg_for_lon(74.0) == 32643


def test_rejects_longitude_outside_pakistan_utm_span():
    with pytest.raises(ValueError):
        utm_epsg_for_lon(80.0)


def test_storage_curve_monotonic_and_units():
    curve = storage_curve_from_array(np.array([[100.0, 101.0], [102.0, 103.0]]), 100.0, 1.0)
    assert curve["storage_m3"].is_monotonic_increasing
    assert curve.iloc[-1]["storage_m3"] > 0
    assert curve.iloc[-1]["water_surface_area_ha"] >= 0


def test_storage_curve_rejects_empty_dem():
    with pytest.raises(ValueError):
        storage_curve_from_array(np.array([[np.nan]]), 100.0, 1.0)
