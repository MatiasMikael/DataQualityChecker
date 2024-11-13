# Installation and Usage Guide – Data Quality Checker

Follow these steps to install, configure, and run the Data Quality Checker project.

## 1. Create the Database and Table

### Create the PostgreSQL Database:

```sql
CREATE DATABASE data_quality_db;
```

### Connect to the Database:

```bash
psql -U postgres -d data_quality_db
```

### Create the customers Table:

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    email VARCHAR(100),
    purchase_amount FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Add Sample Data for Testing:

```sql
INSERT INTO customers (name, age, email, purchase_amount) VALUES
('John Doe', 25, 'john.doe@example.com', 100.0),
('Jane Smith', -5, 'jane.smith@example', 200.0),
('Alice Johnson', 45, NULL, 150.0),
('Bob Brown', 130, 'bob.brown@example.com', 50.0),
('Carol White', 30, 'invalid.email@format', 300.0);
```

## 2. Run the Script

Start the Python script by running the following command:

```bash
python data_quality_checker.py
```

This will schedule a daily data quality check at 04:00.

## 3. Running as a 24/7 Background Service (Optional)

If you would like the script to run continuously in the background, here are instructions for setting it up as a service on both Windows and Linux.

### Windows: Using NSSM to Run as a Service

1. Download and install NSSM ([Non-Sucking Service Manager](https://nssm.cc/download)).

2. Create a service for your script: Open Command Prompt as administrator and run the following command (replace `C:\path\to\your_script.py` with the full path to your script):

   ```bash
   nssm install DataQualityChecker "C:\path\to\python.exe" "C:\path\to\data_quality_checker.py"
   ```

3. Start the service and set it to start automatically on system boot.

### Linux: Using systemd to Run as a Service

1. Create a systemd service file for the script: Create a new file `/etc/systemd/system/data_quality_checker.service` and add the following content:

   ```ini
   [Unit]
   Description=Data Quality Checker

   [Service]
   ExecStart=/usr/bin/python3 /path/to/data_quality_checker.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. Enable and start the service:

   ```bash
   sudo systemctl enable data_quality_checker
   sudo systemctl start data_quality_checker
   ```

The Data Quality Checker will now run in the background 24/7 and perform data quality checks daily at 04:00.