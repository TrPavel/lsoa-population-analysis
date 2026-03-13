"""
Visualisation utilities for LSOA population analysis.
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_england_profile(england_props: pd.Series, save_path: str | None = None):
    """Bar chart of England-wide age band proportions."""
    fig, ax = plt.subplots(figsize=(12, 5))
    england_props.plot(kind="bar", ax=ax, color="steelblue")
    ax.set_title("England: Age Distribution (Proportions)")
    ax.set_ylabel("Proportion of population")
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()


def plot_lsoa_comparison(compare_df: pd.DataFrame, save_path: str | None = None):
    """Grouped bar chart comparing LSOA age profiles against England."""
    fig, ax = plt.subplots(figsize=(14, 6))
    compare_df.plot(kind="bar", ax=ax)
    ax.set_title("Age Distribution by LSOA vs England (Proportions)")
    ax.set_ylabel("Proportion of population")
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()


def plot_distributions(df: pd.DataFrame, save_path: str | None = None):
    """2×2 histogram grid for Total, younger_prop, older_prop, median_age."""
    cols = ["Total", "younger_prop", "older_prop", "median_age"]
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for ax, col in zip(axes.flatten(), cols):
        df[col].hist(bins=60, ax=ax)
        ax.set_xlabel(col)
        ax.set_ylabel("Count of LSOAs")
        ax.set_title(col)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()


def plot_median_age_by_area(df: pd.DataFrame, save_path: str | None = None):
    """Overlaid histograms of median age by area type."""
    bins = range(15, 76, 2)
    fig, ax = plt.subplots(figsize=(10, 6))
    for area, group in df.groupby("AreaType"):
        group["median_age"].plot(
            kind="hist", bins=bins, histtype="step", label=area, ax=ax
        )
    ax.set_xlabel("Median Age")
    ax.set_ylabel("Number of LSOAs")
    ax.set_title("Distribution of Median Age by Area Type")
    ax.legend()
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()


def plot_younger_vs_older(df: pd.DataFrame, save_path: str | None = None):
    """Scatter plot of younger vs older population proportions."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df["younger_prop"], df["older_prop"], s=5, alpha=0.3)
    ax.set_xlabel("Proportion of Younger Residents (0–19)")
    ax.set_ylabel("Proportion of Older Residents (65+)")
    ax.set_title("Younger vs Older Population Proportions across LSOAs")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()


def plot_age_classes_by_area(pivot_df: pd.DataFrame, save_path: str | None = None):
    """Bar chart of unusual age profile classes by area type."""
    fig, ax = plt.subplots(figsize=(10, 6))
    pivot_no_normal = pivot_df.drop(columns=["Normal"], errors="ignore")
    pivot_no_normal.plot(kind="bar", ax=ax)
    ax.set_title("Distribution of Unusual Age Profile Classes by Area Type")
    ax.set_ylabel("Number of LSOAs")
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()
