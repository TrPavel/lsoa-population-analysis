"""LSOA population age structure analysis utilities."""

from .demographics import (
    AGE_ORDER, YOUNGER_COLS, OLDER_COLS, LOWER_BOUNDS, AREA_MAP,
    add_age_proportions, england_proportions, median_age_row,
    add_median_age, add_area_type, classify_age_profile, add_age_class,
)
from .plotting import (
    plot_england_profile, plot_lsoa_comparison, plot_distributions,
    plot_median_age_by_area, plot_younger_vs_older, plot_age_classes_by_area,
)
