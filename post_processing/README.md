# Post-processing

This folder turns raw WRF output into analysis-ready fields used in the Erin paper.

## What each file does

- `bashrc_wrf`  
  Loads modules and environment variables used when compiling/running WRF on OSCER.

- `postproc.sh`  
  Operational shell workflow: sources environment, moves `wrfout_d0*` files, and stitches hourly outputs into `stitchd01_*.nc` / `stitchd02_*.nc` with `ncrcat`.

- `interp_variable.py`  
  Vertically interpolates WRF winds (`U`, `V`) onto specified AGL levels, writes new NetCDF outputs, and preserves core metadata/dimensions needed for downstream analysis.

- `relvort.py`  
  Computes relative vorticity from gridded zonal/meridional wind using latitude/longitude spacing.

- `track_tc.py`  
  Implements the object-based TC tracking algorithm (smoothing, thresholding, spatial continuity masking, centroid tracking through time).

- `trackstorm.py`  
  End-to-end tracking driver: loads interpolated winds, computes relative vorticity, runs `track_tc.object_track`, and writes storm-center latitude/longitude time series to NetCDF.

## What this reproduces

These scripts produce the intermediate products that feed the track and dynamical diagnostics in `figure_reproduction/` (especially track-based and radial composite analyses).

## Data needed

Inputs are stitched WRF NetCDF files and interpolated wind files from Erin simulations (paths currently set to the original HPC archive structure). Outputs are NetCDF files containing interpolated fields and storm tracks.
