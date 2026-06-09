#!/usr/bin/env python3
import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compute hourly diurnal-cycle means from a timestamped CSV.")
    parser.add_argument("--input", required=True, help="Input CSV with columns timestamp,value")
    parser.add_argument("--output", required=True, help="Output CSV path")
    return parser.parse_args()


def load_rows(path: Path) -> dict[int, list[float]]:
    buckets: dict[int, list[float]] = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            timestamp = datetime.fromisoformat(row["timestamp"])
            value = float(row["value"])
            buckets[timestamp.hour].append(value)
    return buckets


def write_output(path: Path, buckets: dict[int, list[float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["hour_utc", "mean_value", "count"])
        for hour in range(24):
            values = buckets.get(hour, [])
            if values:
                writer.writerow([hour, sum(values) / len(values), len(values)])


def main() -> None:
    args = parse_args()
    buckets = load_rows(Path(args.input))
    write_output(Path(args.output), buckets)


if __name__ == "__main__":
    main()
