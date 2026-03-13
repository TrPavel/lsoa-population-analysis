"""
Demographic calculations for LSOA population analysis.

Provides utilities for computing age proportions, estimating median age,
and classifying areas by age structure.
"""

import numpy as np
import pandas as pd


# ──────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────
AGE_ORDER = [
    "Age4Under", "Age5to9", "Age10to14", "Age15to19",
    "Age20to24", "Age25to29", "Age30to34", "Age35to39",
    "Age40to44", "Age45to49", "Age50to54", "Age55to59",
    "Age60to64", "Age65to69", "Age70to74", "Age75to79",
    "Age80to84", "Age85Over",
]

YOUNGER_COLS = ["Age4Under", "Age5to9", "Age10to14", "Age15to19"]
OLDER_COLS = ["Age65to69", "Age70to74", "Age75to79", "Age80to84", "Age85Over"]

LOWER_BOUNDS = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

AREA_MAP = {
    "E06": "Unitary Authorities",
    "E07": "Non-metropolitan Districts",
    "E08": "Metropolitan Districts",
    "E09": "London Boroughs",
}


# ──────────────────────────────────────────────
# Age proportion calculations
# ──────────────────────────────────────────────
def add_age_proportions(df: pd.DataFrame) -> pd.DataFrame:
    """Add younger_prop (0–19) and older_prop (65+) columns to DataFrame."""
    df = df.copy()
    df["younger_prop"] = df[YOUNGER_COLS].sum(axis=1) / df["Total"]
    df["older_prop"] = df[OLDER_COLS].sum(axis=1) / df["Total"]
    return df


def england_proportions(df: pd.DataFrame) -> pd.Series:
    """Compute England-wide age band proportions."""
    age_cols = [c for c in df.columns if c.startswith("Age")]
    totals = df[age_cols].sum()
    return totals / totals.sum()


# ──────────────────────────────────────────────
# Median age estimation
# ──────────────────────────────────────────────
def median_age_row(row: pd.Series) -> float:
    """Estimate median age for a single LSOA using linear interpolation
    within 5-year bands.

    Parameters
    ----------
    row : pd.Series
        Must contain AGE_ORDER columns and 'Total'.

    Returns
    -------
    float
        Estimated median age.
    """
    counts = row[AGE_ORDER].values.astype("float64")
    total = float(row["Total"])
    if total <= 0:
        return float("nan")

    cum = counts.cumsum()
    half = 0.5 * total
    idx = (cum >= half).argmax()

    lower = float(LOWER_BOUNDS[idx])
    prev_cum = 0.0 if idx == 0 else float(cum[idx - 1])
    band_count = float(counts[idx])

    if band_count <= 0:
        return lower

    within = (half - prev_cum) / band_count
    return lower + 5.0 * max(0.0, min(1.0, within))


def add_median_age(df: pd.DataFrame) -> pd.DataFrame:
    """Add estimated median_age column to DataFrame."""
    df = df.copy()
    df["median_age"] = df.apply(median_age_row, axis=1)
    return df


# ──────────────────────────────────────────────
# Area type mapping
# ──────────────────────────────────────────────
def add_area_type(df: pd.DataFrame) -> pd.DataFrame:
    """Map PartOfCode prefixes to human-readable area type labels."""
    df = df.copy()
    df["AreaType"] = df["PartOfCode"].str[:3].map(AREA_MAP)
    return df


# ──────────────────────────────────────────────
# Age profile classification
# ──────────────────────────────────────────────
def classify_age_profile(row: pd.Series) -> str:
    """Classify an LSOA by its age structure.

    Rules:
        - Young Families:    younger_prop > 0.30 and older_prop < 0.10
        - Elderly Areas:     younger_prop < 0.10 and older_prop > 0.30
        - Working-age Zones: younger_prop < 0.15 and older_prop < 0.15
        - Normal:            everything else
    """
    y, o = row["younger_prop"], row["older_prop"]
    if y > 0.30 and o < 0.10:
        return "Young Families"
    elif y < 0.10 and o > 0.30:
        return "Elderly Areas"
    elif y < 0.15 and o < 0.15:
        return "Working-age Zones"
    return "Normal"


def add_age_class(df: pd.DataFrame) -> pd.DataFrame:
    """Add AgeProfileClass column based on classification rules."""
    df = df.copy()
    df["AgeProfileClass"] = df.apply(classify_age_profile, axis=1)
    return df
