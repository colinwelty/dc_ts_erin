#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path


WIDTH = 800
HEIGHT = 400
MARGIN = 50


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a diurnal-cycle line plot to SVG.")
    parser.add_argument("--input", required=True, help="CSV from post_processing/extract_diurnal_cycle.py")
    parser.add_argument("--output", required=True, help="Output SVG path")
    return parser.parse_args()


def read_points(path: Path) -> list[tuple[int, float]]:
    points: list[tuple[int, float]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            points.append((int(row["hour_utc"]), float(row["mean_value"])))
    if not points:
        raise ValueError("No points found in input CSV")
    return sorted(points)


def to_svg_polyline(points: list[tuple[int, float]]) -> tuple[str, float, float]:
    min_y = min(value for _, value in points)
    max_y = max(value for _, value in points)
    y_span = max(max_y - min_y, 1e-9)

    def x_coord(hour: int) -> float:
        return MARGIN + (hour / 23.0) * (WIDTH - 2 * MARGIN)

    def y_coord(value: float) -> float:
        return HEIGHT - MARGIN - ((value - min_y) / y_span) * (HEIGHT - 2 * MARGIN)

    coords = " ".join(f"{x_coord(h):.2f},{y_coord(v):.2f}" for h, v in points)
    return coords, min_y, max_y


def write_svg(path: Path, points: list[tuple[int, float]]) -> None:
    polyline, min_y, max_y = to_svg_polyline(points)
    path.parent.mkdir(parents=True, exist_ok=True)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}">
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="white" />
  <line x1="{MARGIN}" y1="{HEIGHT - MARGIN}" x2="{WIDTH - MARGIN}" y2="{HEIGHT - MARGIN}" stroke="black" />
  <line x1="{MARGIN}" y1="{MARGIN}" x2="{MARGIN}" y2="{HEIGHT - MARGIN}" stroke="black" />
  <polyline fill="none" stroke="navy" stroke-width="2" points="{polyline}" />
  <text x="{WIDTH / 2}" y="{HEIGHT - 10}" text-anchor="middle" font-size="14">UTC Hour</text>
  <text x="15" y="{HEIGHT / 2}" text-anchor="middle" font-size="14" transform="rotate(-90 15 {HEIGHT / 2})">Mean Value</text>
  <text x="{WIDTH - MARGIN}" y="{MARGIN}" text-anchor="end" font-size="12">min={min_y:.3f}, max={max_y:.3f}</text>
</svg>
'''
    path.write_text(svg, encoding="utf-8")


def main() -> None:
    args = parse_args()
    points = read_points(Path(args.input))
    write_svg(Path(args.output), points)


if __name__ == "__main__":
    main()
