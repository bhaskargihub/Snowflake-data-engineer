from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 11, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('daily_etl_pipeline',
         default_args=default_args,
         schedule_interval='0 9 * * *',
         catchup=False) as dag:

    task_upload = PythonOperator(
        task_id='upload_to_s3',
        python_callable=lambda: __import__('scripts.upload_to_s3').upload_to_s3()
    )

    task_load = PythonOperator(
        task_id='load_to_snowflake',
        python_callable=lambda: __import__('scripts.load_to_snowflake').load_to_snowflake(
            user=os.environ.get('SNOW_USER'),
            password=os.environ.get('SNOW_PASSWORD'),
            account=os.environ.get('SNOW_ACCOUNT'),
            database=os.environ.get('SNOW_DATABASE', 'MY_DB'),
            schema=os.environ.get('SNOW_SCHEMA', 'PUBLIC'),
            warehouse=os.environ.get('SNOW_WAREHOUSE', 'COMPUTE_WH')
        )
    )

    task_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='cd /opt/airflow/dbt_project && dbt run'
    )

    task_upload >> task_load >> task_dbt
