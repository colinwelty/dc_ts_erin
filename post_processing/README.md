# Post-processing

This directory contains scripts for converting storm time series into hourly diurnal cycle products used by the paper.

## Script

- `extract_diurnal_cycle.py`:
  - Input CSV columns: `timestamp,value`
  - `timestamp` must be ISO-8601 parseable by Python `datetime.fromisoformat`
  - Output CSV columns: `hour_utc,mean_value,count`
