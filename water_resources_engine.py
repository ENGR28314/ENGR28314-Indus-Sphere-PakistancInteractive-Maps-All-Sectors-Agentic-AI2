"""Curated, source-labelled water-resource reference datasets for IndusSphere.

Figures supplied by the project owner are preserved as historical/reference data.
The module deliberately reports arithmetic inconsistencies rather than silently
changing source rows or presenting them as verified current operational data.
"""
from __future__ import annotations
import pandas as pd


def hill_torrent_table() -> pd.DataFrame:
    rows = [
        ("Federal / Northern Area", "Northern Area", 60700, 149929, 0.940, 1159),
        ("Federal / AJK", "Azad Jammu & Kashmir", 33600, 82992, 0.400, 493),
        ("Federal / FATA (legacy classification)", "FATA", 178700, 441389, 1.500, 1850),
        ("NWFP / KP", "D.I. Khan", 419000, 1034930, 0.800, 986),
        ("NWFP / KP", "FATA (legacy classification; duplicated in source table)", 178700, 441389, 1.500, 1850),
        ("NWFP / KP", "Hazara, Kabul & Bannu", 442300, 1092481, 3.760, 4636),
        ("Punjab", "D.G. Khan", 349700, 863759, 0.854, 1053),
        ("Punjab", "Potohar", 220800, 545376, 1.860, 2293),
        ("Punjab", "Rachna & Chaj Doab", None, None, None, None),
        ("Sindh", "Kirthar Range", 279300, 689871, 0.296, 365),
        ("Sindh", "Karachi", 64560, 159463, 0.094, 116),
        ("Sindh", "Sehwan & Petaro", 207000, 511290, 0.330, 407),
        ("Balochistan", "Indus Basin Component", 837900, 2069613, 4.067, 5015),
        ("Balochistan", "Kharan", 1060500, 2619435, 0.789, 973),
        ("Balochistan", "Makran", 2781500, 6870305, 3.000, 3690),
    ]
    return pd.DataFrame(rows, columns=["source_group", "area", "culturable_wasteland_ha", "culturable_wasteland_acres", "annual_conservation_potential_maf", "annual_conservation_potential_mcm"])


def hill_torrent_subtotals() -> pd.DataFrame:
    return pd.DataFrame([
        ("Federal subtotal (includes FATA)", 273000, 674310, 2.840, 3502),
        ("NWFP / KP subtotal (also includes FATA)", 1040000, 2568800, 6.060, 7472),
        ("Punjab subtotal", 570500, 1409135, 2.714, 3346),
        ("Sindh subtotal", 550860, 1360624, 0.720, 888),
        ("Balochistan subtotal", 4679900, 11559353, 7.856, 9678),
        ("Source grand total (FATA counted once)", 6935560, 17130833, 18.690, 23036),
    ], columns=["area_group", "hectares", "acres", "potential_maf", "potential_mcm"])


def proposed_indus_storage() -> pd.DataFrame:
    rows = [
        ("Bunji", 0.06, "Feasibility study completed; detailed design and tender documents in progress"),
        ("Diamer Bhasha", 6.40, "Ready for implementation (as stated in supplied historical table)"),
        ("Dasu", 0.69, "Feasibility study completed; detailed design and tender documents in progress"),
        ("Thakot HPP", 0.16, "PC-II submitted for approval"),
        ("Pattan", 0.06, "PC-II approved"),
        ("Yulbo", 0.12, "Desk study and field reconnaissance done"),
        ("Tungus", 0.05, "Desk study initiated"),
        ("Skardu", 5.50, "Desk study initiated"),
        ("Shyok / Yugo", 5.00, "Desk study initiated"),
    ]
    return pd.DataFrame(rows, columns=["project", "storage_maf", "status_as_supplied"])


def population_water_availability() -> pd.DataFrame:
    return pd.DataFrame([
        (1951, 34, 5260), (2010, 172, 1038), (2020, 204, 877), (2025, 221, 809),
    ], columns=["year", "population_million", "per_capita_availability_m3_year"])


def reservoir_sedimentation() -> pd.DataFrame:
    # Values transcribed from the cited historical table: 2009 capacity/loss,
    # then cumulative loss estimates for 2012 and 2025.
    return pd.DataFrame([
        ("Tarbela", 9.68, 6.78, 2.90, 3.18, 4.30),
        ("Mangla", 5.34, 4.46, 0.88, 0.90, 1.14),
        ("Chashma", 0.72, 0.37, 0.35, 0.29, 0.38),
    ], columns=["reservoir", "original_capacity_maf", "remaining_capacity_2009_maf", "loss_2009_maf", "cumulative_loss_2012_maf", "cumulative_loss_2025_maf"])


def validate_reference_totals() -> dict:
    hill = hill_torrent_table()
    projects = proposed_indus_storage()
    sed = reservoir_sedimentation()
    pop = population_water_availability()
    # The FATA row appears twice in the supplied regional subtotals, but the
    # source grand total is reconciled by counting the area/potential only once.
    dedup_ha = hill["culturable_wasteland_ha"].sum(skipna=True) - 178700
    dedup_maf = hill["annual_conservation_potential_maf"].sum(skipna=True) - 1.5
    return {
        "hill_torrent_deduplicated_ha": int(dedup_ha),
        "hill_torrent_deduplicated_maf": round(float(dedup_maf), 3),
        "project_storage_list_sum_maf": round(float(projects["storage_maf"].sum()), 2),
        "project_storage_reported_total_maf": 18.5,
        "sedimentation_original_total_maf": round(float(sed["original_capacity_maf"].sum()), 2),
        "sedimentation_2009_loss_total_maf": round(float(sed["loss_2009_maf"].sum()), 2),
        "sedimentation_2012_loss_total_maf": round(float(sed["cumulative_loss_2012_maf"].sum()), 2),
        "sedimentation_2025_loss_total_maf": round(float(sed["cumulative_loss_2025_maf"].sum()), 2),
        "population_years": pop["year"].tolist(),
    }
