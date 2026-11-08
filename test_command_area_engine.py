import unittest
import pandas as pd
from command_area_engine import validate_command_areas, add_command_area_indicators

class CommandAreaTests(unittest.TestCase):
    def test_valid_areas_and_ratio(self):
        df = pd.DataFrame([{"name":"Example Dam","gca_ha":100000,"cca_ha":75000}])
        out = add_command_area_indicators(df)
        self.assertEqual(out.loc[0,"validation_status"], "Valid")
        self.assertAlmostEqual(out.loc[0,"cca_to_gca_pct"], 75.0)
        self.assertEqual(out.loc[0,"non_cultivable_command_area_ha"], 25000)

    def test_cca_cannot_exceed_gca(self):
        df = pd.DataFrame([{"name":"Example Dam","gca_ha":100,"cca_ha":101}])
        out = validate_command_areas(df)
        self.assertEqual(out.loc[0,"validation_status"], "Invalid: CCA exceeds GCA")

    def test_missing_values_are_not_invented(self):
        df = pd.DataFrame([{"name":"Example Dam","gca_ha":None,"cca_ha":None}])
        out = add_command_area_indicators(df)
        self.assertTrue(pd.isna(out.loc[0,"cca_to_gca_pct"]))
        self.assertEqual(out.loc[0,"validation_status"], "Awaiting data")

if __name__ == "__main__":
    unittest.main()
