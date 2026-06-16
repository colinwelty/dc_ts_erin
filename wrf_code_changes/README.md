# WRF code changes

This folder documents the WRF v4.5.0 modifications and runtime files used for the Erin control/imposed experiments.

## File-by-file overview

- `Registry.EM_COMMON_imp`  
  Registry edits that add the imposed surface-flux input variables (`HFX_INPUT`, `LH_INPUT`, `QFX_INPUT`) as state/IO fields.

- `module_surface_driver.F_imp`  
  Surface driver variant wired to accept imposed flux inputs during integration.

- `module_radiation_driver_diurnalCOPY.F`  
  Radiation driver variant used for the diurnal-cycle experiment configuration.

- `namelist.input.TSErincontrol`  
  Control experiment namelist used to generate baseline Erin output and diagnostics.

- `namelist.input.TSErinImposed`  
  Imposed-flux experiment namelist, including `auxinput7` settings used to read external flux forcing.

- `impose.pdf`  
  Experiment notes and implementation rationale for the imposed-flux method.

## What this reproduces

These files reproduce the model-side setup needed to generate the simulation families compared throughout the paper (control, diurnal, and imposed variants).

## Usage note

The modified source files use `_imp`/copy naming in this repository for documentation. For a real WRF build, place the edited code into the expected WRF filenames before compiling.
