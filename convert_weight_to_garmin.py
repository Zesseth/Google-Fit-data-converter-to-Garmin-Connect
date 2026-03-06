#!/usr/bin/env python3
# Copyright (C) 2026  Jesse Lahtela
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Convert Google Fit weight data to a Garmin Connect compatible CSV file.

Reads weight data exported via Google Takeout and converts it into a
Fitbit-format CSV that Garmin Connect can import.

Usage:
    python convert_weight_to_garmin.py
    python convert_weight_to_garmin.py -i path/to/fit_weight.json
    python convert_weight_to_garmin.py -i input.json -o output.csv --timezone US/Eastern

If no -i/--input is provided, the script will prompt for the path interactively.
"""

import argparse
import json
import sys
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

# Default file paths
SCRIPT_DIR = Path(__file__).parent
DEFAULT_OUTPUT = SCRIPT_DIR / "garmin_weight_import.csv"
DEFAULT_TIMEZONE = "Europe/Helsinki"


def convert_nanos_to_date(nanos: int, tz: ZoneInfo) -> str:
    """Convert nanosecond timestamp to a date string (YYYY-MM-DD)."""
    seconds = nanos / 1_000_000_000
    dt = datetime.fromtimestamp(seconds, tz=tz)
    return dt.strftime("%Y-%m-%d")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert Google Fit weight data to a Garmin Connect compatible CSV file."
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default=None,
        help="Path to the Google Fit weight JSON file",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Path for the output CSV file (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--timezone",
        default=DEFAULT_TIMEZONE,
        help=f"Timezone for date conversion (default: {DEFAULT_TIMEZONE})",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # If no input file was provided, prompt the user
    if args.input is None:
        print("No input file specified.")
        raw = input("Enter the path to the Google Fit weight JSON file: ").strip()
        if not raw:
            print("ERROR: No path provided.", file=sys.stderr)
            sys.exit(1)
        args.input = Path(raw)

    try:
        tz = ZoneInfo(args.timezone)
    except KeyError:
        print(f"ERROR: Unknown timezone: {args.timezone}", file=sys.stderr)
        sys.exit(1)

    input_file: Path = args.input
    output_file: Path = args.output

    # Check that the input file exists
    if not input_file.exists():
        print(f"ERROR: Input file not found: {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read Google Fit JSON
    print(f"Reading: {input_file}")
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Collect weight data: {date: (timestamp_nanos, weight_kg)}
    weight_by_date: dict[str, tuple[int, float]] = {}

    for point in data.get("Data Points", []):
        timestamp_nanos = point.get("startTimeNanos", 0)
        weight_kg = point.get("fitValue", [{}])[0].get("value", {}).get("fpVal")

        if weight_kg is None:
            continue

        date_str = convert_nanos_to_date(timestamp_nanos, tz)

        # Keep the latest measurement per day
        if date_str not in weight_by_date or timestamp_nanos > weight_by_date[date_str][0]:
            weight_by_date[date_str] = (timestamp_nanos, weight_kg)

    if not weight_by_date:
        print("ERROR: No weight data found in the input file.", file=sys.stderr)
        sys.exit(1)

    # Sort by date
    sorted_dates = sorted(weight_by_date.keys())

    # Write Fitbit-format CSV (Garmin Connect can import this format)
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        f.write("Body\n")
        f.write("Date,Weight,BMI,Fat\n")
        for date_str in sorted_dates:
            weight = round(weight_by_date[date_str][1], 1)
            f.write(f"{date_str},{weight},0,0\n")

    print(f"\nConverted {len(sorted_dates)} weight measurements.")
    print(f"Date range: {sorted_dates[0]} — {sorted_dates[-1]}")
    print(f"\nOutput saved to: {output_file}")
    print("\nNext steps:")
    print("1. Go to https://connect.garmin.com/modern/import-data")
    print("2. Click 'Import Data' and select the file: garmin_weight_import.csv")
    print("3. Choose 'Kilograms (kg)' as the unit")


if __name__ == "__main__":
    main()
