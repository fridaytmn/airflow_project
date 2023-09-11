from datetime import datetime
import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from ingestion_script import ingest_data

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow")

#url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet'
URL_PREFIX = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
URL_TEMPLATE = URL_PREFIX + "yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet"
OPTPUT_TEMPLATE = AIRFLOW_HOME + "/output_{{ execution_date.strftime(\'%Y-%m\') }}.parquet"
TABLE_TEMPLATE = "yellow_taxi_data"


workflow = DAG(
    dag_id='IngestionDag',
    start_date=datetime(2023,1,1),
    schedule='0 6 2 * *'
)

with workflow:
    
    curl_task = BashOperator(
        task_id='curl',
        bash_command=f'curl -sSL {URL_TEMPLATE} > {OPTPUT_TEMPLATE}'
    )
    
    load_task = PythonOperator(
        task_id='load',
        python_callable=ingest_data,
        op_kwargs=dict(
            parquet_file=OPTPUT_TEMPLATE,
            table_name=TABLE_TEMPLATE
        )
    )
    
    # external_task_sensor = ExternalTaskSensor(
    #     task_id='external_task_sensor',
    #     timeout=180,
    #     retries=2,
    #     external_task_id='check_pg_connect',
    #     external_dag_id='check_pg'
    # )
    
curl_task >> load_task