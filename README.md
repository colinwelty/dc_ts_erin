# The Diurnal Cycle in Tropical Storm Erin (2007)

Repository for AMS paper submission materials for **The Diurnal Cycle in Tropical Storm Erin (2007)**.

## Repository layout

- `post_processing/` - scripts to transform model/output data into analysis-ready diurnal-cycle products.
- `wrf_code_changes/` - patch files and notes documenting WRF source changes used in experiments.
- `figure_reproduction/` - scripts to regenerate publication figures from processed products.

## Quick start

1. Run post-processing:
   ```bash
   python post_processing/extract_diurnal_cycle.py --input path/to/timeseries.csv --output out/diurnal_cycle.csv
   ```
2. Reproduce figure:
   ```bash
   python figure_reproduction/plot_diurnal_cycle_svg.py --input out/diurnal_cycle.csv --output out/diurnal_cycle.svg
   ```
3. Review WRF modifications:
   ```bash
   ls wrf_code_changes
   ```
