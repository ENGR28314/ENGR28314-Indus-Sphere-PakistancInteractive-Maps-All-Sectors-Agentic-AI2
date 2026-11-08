import pandas as pd
from water_resources_engine import proposed_indus_storage


def test_proposed_storage_projects_have_positive_values():
    df = proposed_indus_storage()
    assert len(df) == 9
    assert (df["storage_maf"] > 0).all()


def test_listed_storage_sum_is_18_04_maf():
    assert round(proposed_indus_storage()["storage_maf"].sum(), 2) == 18.04


def test_flow_reference_has_required_groups():
    df = pd.read_csv("average_annual_indus_basin_flows_reference.csv")
    assert {"river_group", "average_annual_flow_maf", "reference_basis"}.issubset(df.columns)
    assert set(df["river_group"]) >= {"Western Rivers (Indus, Jhelum, Chenab)", "Eastern Rivers (Ravi, Sutlej, Beas)"}
