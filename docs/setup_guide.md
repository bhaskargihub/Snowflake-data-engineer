# Setup Guide - Snowflake Data Engineer Project

This guide walks you through setting up the project (beginner-friendly).

## 1. Prerequisites (install once)
- Python 3.9+
- Git
- AWS account and IAM user with S3 access
- Snowflake account
- Power BI (optional: for visualization)

## 2. Clone the repo
```bash
git clone <your-repo-url>
cd Snowflake-data-engineer-full
```

## 3. Install Python dependencies
```bash
python -m pip install -r requirements.txt
```

## 4. Configure AWS credentials
```bash
aws configure
# or set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY env vars
```

## 5. Create S3 bucket (one-time)
- Use AWS console or CLI:
```bash
aws s3 mb s3://my-snowflake-bucket
```

## 6. Snowflake setup (one-time)
- Login to Snowflake worksheet and run scripts in `sql/` in order:
  1. `00_create_file_format.sql`
  2. `01_create_stage_integration_instructions.sql` (follow instructions and create integration in Snowflake + AWS)
  3. `02_create_stage.sql` (after integration is ready)
  4. `03_create_table.sql`
- The `01_create_stage_integration_instructions.sql` includes AWS steps — follow Snowflake docs to create the IAM Role and trust.

## 7. Test a manual load to Snowflake
- Upload a local sample file to S3:
```bash
python scripts/upload_to_s3.py
```
- Run COPY INTO via snowsql or via script:
```bash
python scripts/load_to_snowflake.py
```

## 8. DBT setup
- Copy `dbt_project/profiles.yml.example` to your user `~/.dbt/profiles.yml` and fill credentials.
- Run:
```bash
cd dbt_project
dbt deps
dbt debug
dbt run
```

## 9. Airflow setup (local)
- Initialize and run Airflow:
```bash
export AIRFLOW_HOME=~/airflow
pip install apache-airflow
airflow db init
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin
# Put this repo's dags folder into $AIRFLOW_HOME/dags or configure AIRFLOW__CORE__DAGS_FOLDER
airflow webserver -p 8080
airflow scheduler
```
- Set environment variables for Snowflake credentials in the environment where Airflow runs:
```bash
export SNOW_USER=your_user
export SNOW_PASSWORD=your_password
export SNOW_ACCOUNT=your_account
export SNOW_DATABASE=MY_DB
export SNOW_SCHEMA=PUBLIC
export SNOW_WAREHOUSE=COMPUTE_WH
```

## 10. Power BI
- In Power BI Desktop: Get Data -> Snowflake -> enter account, warehouse and database.
- Choose the transformed table and build dashboards.

## 11. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - full Snowflake ETL project"
git remote add origin https://github.com/bhaskargihub/Snowflake-data-engineer.git
git branch -M main
git push -u origin main
```

## Troubleshooting
- If COPY INTO fails, check file path in stage and permissions on S3 role.
- Use `airflow logs -f <dag_run>` to debug DAG runs.
