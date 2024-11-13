import pandas as pd
from sqlalchemy import create_engine
import re
import logging
import schedule
import time
from datetime import datetime

# Configure logging to write to a file
logging.basicConfig(
    filename="data_quality_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Define the database connection using SQLAlchemy, without password
DATABASE = "postgresql://postgres@localhost:5433/data_quality_db"
engine = create_engine(DATABASE)

def log_and_print(message):
    """Logs and prints messages to console and log file."""
    print(message)
    logging.info(message)

def check_missing_values(df):
    missing_values = df.isnull().sum()
    missing_columns = missing_values[missing_values > 0]
    if not missing_columns.empty:
        log_and_print("Missing values per column:\n" + str(missing_columns))
    else:
        log_and_print("No missing values found.")

def check_age_range(df):
    invalid_ages = df[(df['age'] < 0) | (df['age'] > 120)]
    if not invalid_ages.empty:
        log_and_print("Invalid ages found:\n" + str(invalid_ages))
    else:
        log_and_print("All ages are within the valid range.")

def check_email_format(df):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    invalid_emails = df[~df['email'].str.contains(email_pattern, na=False)]
    if not invalid_emails.empty:
        log_and_print("Invalid emails found:\n" + str(invalid_emails))
    else:
        log_and_print("All emails are in a valid format.")

def run_data_quality_checks():
    """Fetches data and runs all quality checks, logging results."""
    log_and_print("Running data quality checks...")
    with engine.connect() as connection:
        df = pd.read_sql("SELECT * FROM customers", connection)
    check_missing_values(df)
    check_age_range(df)
    check_email_format(df)
    log_and_print("Data quality checks completed.")

# Schedule the task to run daily at 04:00
schedule.every().day.at("04:00").do(run_data_quality_checks)

log_and_print("Data quality checker scheduled to run daily at 04:00.")

# Loop to keep the script running and check schedule
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute before checking again
