# Figure reproduction

This directory contains notebook-based workflows used to generate Erin analysis figures.

## Files

- `obsdata.ipynb`
  - Loads NCEP Stage IV precipitation, Mesonet station data, and WRF output.
  - Builds publication figure panels comparing observed precipitation/wind and WRF-derived wind fields.
  - Includes plotting sections for both publication-ready figures and intermediate diagnostics.

- `plot_era5.ipynb`
  - Loads ERA5 pressure-level and surface datasets for Erin.
  - Produces publication figures (4-panel precipitable water and vorticity plots) plus additional diagnostic maps across pressure levels.
  - Contains reusable plotting functions and extra exploratory analyses not all used in the final paper.

- `README.md`
  - Documents the purpose of files in this directory.
 
## Tips

Make sure to replace file paths with designated file paths for your workflow. For this project, output exceeds 250 GB for each simulation. Therefore, output data is not included in this repository.
