import unittest
from water_resources_engine import (
    hill_torrent_table, proposed_indus_storage, population_water_availability,
    reservoir_sedimentation, validate_reference_totals,
)

class WaterResourcesReferenceTests(unittest.TestCase):
    def test_hill_torrent_deduplicated_total_matches_source_grand_total(self):
        totals = validate_reference_totals()
        self.assertEqual(totals["hill_torrent_deduplicated_ha"], 6935560)
        self.assertAlmostEqual(totals["hill_torrent_deduplicated_maf"], 18.69)

    def test_proposed_storage_sum_flags_reported_total_difference(self):
        totals = validate_reference_totals()
        self.assertAlmostEqual(totals["project_storage_list_sum_maf"], 18.04)
        self.assertNotEqual(totals["project_storage_list_sum_maf"], totals["project_storage_reported_total_maf"])

    def test_population_series_and_threshold_gap(self):
        df = population_water_availability()
        self.assertEqual(df["population_million"].tolist(), [34, 172, 204, 221])
        self.assertEqual(df["per_capita_availability_m3_year"].tolist(), [5260, 1038, 877, 809])
        self.assertEqual(1000 - int(df.loc[df.year == 2025, "per_capita_availability_m3_year"].iloc[0]), 191)

    def test_sedimentation_totals_reconcile(self):
        totals = validate_reference_totals()
        self.assertAlmostEqual(totals["sedimentation_original_total_maf"], 15.74)
        self.assertAlmostEqual(totals["sedimentation_2009_loss_total_maf"], 4.13)
        self.assertAlmostEqual(totals["sedimentation_2012_loss_total_maf"], 4.37)
        self.assertAlmostEqual(totals["sedimentation_2025_loss_total_maf"], 5.82)

    def test_required_reference_tables_are_nonempty(self):
        self.assertGreater(len(hill_torrent_table()), 0)
        self.assertGreater(len(proposed_indus_storage()), 0)
        self.assertGreater(len(reservoir_sedimentation()), 0)

if __name__ == "__main__":
    unittest.main()
