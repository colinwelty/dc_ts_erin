# Cache files

This folder contains precomputed pickle (`.pkl`) outputs generated from large WRF analyses.

## What the cache files represent

Most filenames follow this pattern:

`<run>_<quantity>_<aggregation>.pkl`

- **Run tags**: `control`, `diurnal`, `d_imp1` (and related imposed variants)
- **Quantities**: `avor`, `theta`, `theta_e`, `rh`, `wa`, `rain`, `vortbudget`
- **Aggregations**: fixed-radius composites, RMW radial bins, and layer-specific budget terms (for example `0to1000m` and `1000to5000m`)

## Why these are provided

Several notebooks (especially vorticity-budget and radial diagnostics) are expensive to recompute from raw model output. These caches let you reproduce key figures quickly without reprocessing terabyte-scale WRF files.

## Data expectations

The cache files are analysis-ready derived products, not raw model output. Use them as reproducibility inputs for plotting notebooks.
