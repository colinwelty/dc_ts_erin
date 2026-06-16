# Figure reproduction

This directory contains notebooks used to recreate the paper figures and supporting diagnostics.

## Notebook guide

- `obsdata.ipynb`  
  Builds observation-focused panels using NCEP Stage IV precipitation, Mesonet station data, and model comparison fields.

- `plot_era5.ipynb`  
  Loads ERA5 pressure-level and surface fields and reproduces large-scale environmental maps used in the manuscript.

- `rainfall.ipynb`  
  Reproduces WRF vs Stage IV rainfall comparison maps/panels for Erin.

- `rainfallrate.ipynb`  
  Computes and plots rainfall-rate evolution diagnostics (including lag/correlation-style comparisons across experiments).

- `plottrack.ipynb`  
  Plots storm tracks from post-processed track files and compares simulations with best-track references.

- `LLJ.ipynb`  
  Produces low-level jet cross-section diagnostics from ERA5 and WRF fields over the study region.

- `vadvsERA5.ipynb`  
  Compares radar VAD wind profiles with ERA5 regional wind structure.

- `vortbudget_plot.ipynb`  
  Reproduces vorticity-budget figures; can build/load cached budget terms and generate manuscript-ready panels.

## What this reproduces

Together, these notebooks recreate the main figure set for Erin: track evolution, rainfall structure, environmental context, LLJ behavior, and vorticity-budget interpretation.

## Data needed

Most notebooks expect local copies of:

- WRF output (raw and post-processed)
- ERA5 pressure/surface datasets
- NCEP Stage IV precipitation
- Mesonet and/or radar-derived products
- Cached `.pkl` files from `cache/` (for faster reproduction of heavy diagnostics)

Update hard-coded file paths before running.
