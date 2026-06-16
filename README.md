# dc_ts_erin

This repository contains the code and supporting data used to produce analyses for **The Diurnal Cycle in Tropical Storm Erin (2007)** (Welty et al., 2026).

The workflow is split into three parts:

1. **`wrf_code_changes/`**: source-level WRF v4.5.0 edits and Erin namelists used to run control and imposed-flux experiments.
2. **`post_processing/`**: scripts that stitch model outputs, interpolate variables, and derive storm-center tracks from relative vorticity.
3. **`figure_reproduction/`**: notebooks that reproduce manuscript figures (rainfall, ERA5 environment, LLJ, tracks, and vorticity-budget diagnostics).

A small subset of derived analysis products is included in **`cache/`** so key figure workflows can run without shipping the full model archive.

## Data summary

Full simulation output is very large (6 simulations, >1 TB total), so this repository includes only representative reproducibility data:

- **`data/`**: observation-side files used by notebooks, primarily NCEP Stage IV precipitation files for Erin dates plus source README metadata.
- **`cache/`**: precomputed `.pkl` products (radial composites, layer means, and vorticity-budget terms) for control/diurnal/imposed experiments.

Most scripts and notebooks still point to the original HPC paths used in production. To rerun locally, replace those paths with your own file locations.

For questions about workflow, data provenance, or expected outputs, contact Colin Welty (colinwelty@ou.edu).
