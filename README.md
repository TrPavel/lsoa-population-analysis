# England LSOA Population Age Structure Analysis

Statistical analysis of demographic age profiles across ~33,000 Lower Layer Super Output Areas (LSOAs) in England, exploring how local age structures differ from the national average and what drives those differences.

## Key Findings

- England's national median age is approximately **40 years**, confirmed by both population-level and LSOA-level estimates
- **London Boroughs** skew youngest (median age 30–38), while **Non-metropolitan Districts** skew oldest (45–50)
- A clear **triangular pattern** emerges when plotting younger vs older population proportions — reflecting the compositional constraint that age groups must sum to 1
- Rule-based classification identifies **1,933 "Young Family"** areas, **620 "Working-age Zones"**, and **89 "Elderly Areas"** among 33,755 LSOAs

## Dataset

The analysis uses LSOA-level census data containing:

- **~33,000 LSOAs** across England
- **18 five-year age bands** (0–4 through 85+) with population counts
- Area type codes (Unitary Authorities, Non-metropolitan Districts, Metropolitan Districts, London Boroughs)

> The dataset file (`LSOA_data.csv`) is included in the repository under `data/`.

## Project Structure

```
├── README.md
├── data/
│   └── LSOA_data.csv           # Census age-band data for ~33,000 LSOAs
├── notebooks/
│   └── analysis.ipynb          # Full analysis with outputs
├── src/
│   ├── __init__.py
│   ├── demographics.py         # Age proportion calculations + median age estimation
│   └── plotting.py             # Visualisation utilities
├── figures/
│   ├── england_age_profile.png
│   ├── lsoa_comparison.png
│   ├── distributions.png
│   ├── median_age_by_area.png
│   ├── younger_vs_older.png
│   └── age_classes_by_area.png
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Analysis Overview

### 1. National Age Profile
Computed England-wide proportions for each 5-year age band. The distribution is middle-heavy with two peaks around 30–39 and 50–59, with steady decline after 60.

### 2. Local vs National Comparison
Compared three contrasting LSOAs against the England average:
- **Bury 026E** — elevated child proportions (0–14)
- **Dorset 024A** — strongly skewed towards 65+ (retirement area)
- **Birmingham 014E** — elevated working-age bands (30–39)

### 3. Derived Metrics
For each LSOA, computed:
- **younger_prop** — proportion aged 0–19
- **older_prop** — proportion aged 65+
- **median_age** — estimated via linear interpolation within 5-year bands

### 4. Area Type Comparison
Overlaid median age distributions across four area types, revealing a clear urban–rural age gradient: London Boroughs youngest → Non-metropolitan Districts oldest.

### 5. Demographic Classification
Rule-based labelling of LSOAs into Young Families, Elderly Areas, Working-age Zones, and Normal — mapped against area types to show how demographic extremes concentrate geographically.

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)

## Setup

```bash
git clone https://github.com/TrPavel/lsoa-population-analysis.git
cd lsoa-population-analysis
pip install -r requirements.txt

# data/LSOA_data.csv is already included — just run:
jupyter notebook notebooks/analysis.ipynb
```

## License

[MIT](LICENSE)
