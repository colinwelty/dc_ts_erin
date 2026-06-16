# Data directory

This folder stores observation-side data and source metadata used for figure reproduction.

## What is included

- `ST4.*` files: NCEP Stage IV precipitation analyses for Erin dates (hourly, 6-hour, and 24-hour accumulation products where available).
- `katz_stageIV_readme.txt`, `katz_missing_data.txt`, `README-info-21_093.txt`: source documentation and known-missing-data notes for Stage IV dataset 21.093.
- `allstations20070819.csv`: station-based supporting data used in observation comparison workflows.

## How the repository uses this data

Notebooks in `figure_reproduction/` use these files to reproduce rainfall and observation-vs-model comparisons.

## Data scope

This is a partial reproducibility subset. Full project workflows also depend on large WRF and ERA5 datasets stored outside this repository.
