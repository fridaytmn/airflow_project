from datetime import datetime
import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow")

url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet'
URL_PREFIX = "https://d37ci6vzurychx.cloudfront.net/trip-data"
URL_TEMPLATE = URL_PREFIX + "yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet"
OPTPUT_TEMPLATE = AIRFLOW_HOME + "/output_{{ execution_date.strftime(\'%Y-%m\') }}.parquet"
TABLE_TEMPLATE = "yellow_taxi_{{ execution_date.strftime(\'%Y-%m\') }}"


workflow = DAG(
    dag_id='IngestionDag',
    start_date=datetime(2023,1,1),
    schedule='0 6 2 * *'
)

with workflow:
    
    curl_task = BashOperator(
        task_id='curl',
        # bash_command=f'curl -sSL {url} > output.parquet'
        bash_command='echo " {{ ds }} {{ execution_date.strftime(\'%Y-%m\') }}"'
    )
    
    load_task = BashOperator(
        task_id='load',
        bash_command='echo'
    )
    
curl_task >> load_task