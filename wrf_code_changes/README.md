# WRF code changes

This directory stores reproducible WRF source-level modifications for Erin experiments.

## Contents

- `erin_diurnal_cycle.patch`: patch documenting added diurnal-cycle diagnostics in WRF output.

Apply with:

```bash
cd /path/to/WRF
patch -p1 < /path/to/dc_ts_erin/wrf_code_changes/erin_diurnal_cycle.patch
```
