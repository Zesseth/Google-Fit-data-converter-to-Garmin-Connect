# Google Fit Data Converter to Garmin Connect

Convert weight data exported from Google Fit (via Google Takeout) into a CSV file that can be imported into Garmin Connect.

## Table of Contents

- [Installation](#installation)
- [How to Get Your Google Fit Data](#how-to-get-your-google-fit-data)
- [Usage](#usage)
- [How to Upload Data to Garmin Connect](#how-to-upload-data-to-garmin-connect)
- [License](#license)

---

## Installation

### Requirements

- Python 3.9 or newer (the script uses the built-in `zoneinfo` module introduced in Python 3.9)
- **Windows or minimal containers only:** `zoneinfo` relies on the operating system's time zone database, which is not bundled with Python on Windows or in some minimal container images. If you get a `ZoneInfoNotFoundError`, install the `tzdata` package:

  ```bash
  pip install tzdata
  ```

  macOS and most Linux distributions include a system time zone database, so no extra package is needed there.

### Steps

1. **Clone or download this repository:**

   ```bash
   git clone https://github.com/Zesseth/Google-Fit-data-converter-to-Garmin-Connect.git
   cd Google-Fit-data-converter-to-Garmin-Connect
   ```

2. **Verify your Python version:**

   ```bash
   python3 --version
   ```

   The output should show Python 3.9 or newer.

---

## How to Get Your Google Fit Data

1. Go to [Google Takeout](https://takeout.google.com/).
2. Click **Deselect all** to start with a clean selection.
3. Scroll down and check **Fit** (Google Fit).
4. Click **Next step**, choose your preferred file format and delivery method, then click **Create export**.
5. Download the archive when it is ready and extract it.
6. Navigate to the extracted folder. The weight data file is typically located at:

   ```
   Takeout/Fit/All Data/derived_com.google.weight_com.google.android.gms_merged.json
   ```

   The exact file name may vary slightly depending on your export, but it will be a `.json` file inside the `Fit/All Data/` folder containing the word `weight`.

---

## Usage

Run the script from a terminal. If you do not provide an input file path, the script will prompt you for one.

### Basic usage (interactive prompt)

```bash
python3 convert_weight_to_garmin.py
```

### Specify the input file

```bash
python3 convert_weight_to_garmin.py -i path/to/fit_weight.json
```

### Specify input, output, and timezone

```bash
python3 convert_weight_to_garmin.py -i input.json -o output.csv --timezone US/Eastern
```

### All options

| Option | Description | Default |
|---|---|---|
| `-i`, `--input` | Path to the Google Fit weight JSON file | Interactive prompt |
| `-o`, `--output` | Path for the output CSV file | `garmin_weight_import.csv` (next to the script) |
| `--timezone` | Timezone for date conversion (e.g. `US/Eastern`, `Europe/London`) | `Europe/Helsinki` |

After a successful run the script prints the number of measurements converted, the date range, and the path to the output file.

---

## How to Upload Data to Garmin Connect

1. Open [Garmin Connect](https://connect.garmin.com/modern/import-data) and sign in to your account.
2. Click **Import Data**.
3. Click **Browse** and select the generated CSV file (default name: `garmin_weight_import.csv`).
4. Select **Kilograms (kg)** as the unit (the script stores weight values in kg).
5. Click **Import Data** to complete the upload.

Your historical weight entries will appear in the **Health Stats** section of Garmin Connect shortly after the import.

---

## License

This project is licensed under the **GNU General Public License v3.0 or later (GPL-3.0-or-later)**.

You are free to use, modify, and distribute this software under the terms of the GPL-3.0-or-later license. See the [LICENSE](LICENSE) file for the full license text.
