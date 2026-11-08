"""Command-area validation and derived indicators for dam/irrigation commands.

GCA and CCA are stored in hectares. Missing figures remain missing; this
module never fills them with estimated or fabricated values.
"""
import pandas as pd


def validate_command_areas(df: pd.DataFrame) -> pd.DataFrame:
    required = {"name", "gca_ha", "cca_ha"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    out = df.copy()
    out["gca_ha"] = pd.to_numeric(out["gca_ha"], errors="coerce")
    out["cca_ha"] = pd.to_numeric(out["cca_ha"], errors="coerce")
    out["validation_status"] = "Awaiting data"
    both = out["gca_ha"].notna() & out["cca_ha"].notna()
    out.loc[both & (out["gca_ha"] < 0), "validation_status"] = "Invalid: negative GCA"
    out.loc[both & (out["cca_ha"] < 0), "validation_status"] = "Invalid: negative CCA"
    out.loc[both & (out["cca_ha"] > out["gca_ha"]), "validation_status"] = "Invalid: CCA exceeds GCA"
    valid = both & (out["gca_ha"] >= 0) & (out["cca_ha"] >= 0) & (out["cca_ha"] <= out["gca_ha"])
    out.loc[valid, "validation_status"] = "Valid"
    return out


def add_command_area_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = validate_command_areas(df)
    out["cca_to_gca_pct"] = (out["cca_ha"] / out["gca_ha"] * 100).where(out["gca_ha"] > 0)
    out["non_cultivable_command_area_ha"] = (out["gca_ha"] - out["cca_ha"]).where(out["validation_status"] == "Valid")
    return out
