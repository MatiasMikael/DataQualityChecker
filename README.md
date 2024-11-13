# Data Quality Checker

Data Quality Checker is a Python-based tool designed to perform daily data quality checks on data stored in a PostgreSQL database. The tool runs scheduled quality checks at 04:00 daily and logs results to a file, making it suitable for monitoring data quality in data warehouses.

## Features

- Checks for missing values
- Validates age values within a reasonable range
- Ensures proper email format
- Logs results to a file and runs checks automatically on schedule

## Quick Start Guide

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the program:
   ```bash
   python data_quality_checker.py
   ```

The script will run in the background and perform data checks daily at 04:00.

## Installation and Usage

For detailed installation and setup instructions, please see [INSTALLATION.md](./INSTALLATION.md).

## Running as a 24/7 Background Service

If you wish to run the script as a 24/7 background service, refer to the instructions in INSTALLATION.md.

## License

This project is licensed under the MIT License.
