from datetime import datetime
import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow")

workflow = DAG(
    dag_id='IngestionDag',
    start_date=datetime(2023,1,1),
    schedule_interval='0 6 2 * *'
)

with workflow:
    
    curl_task = BashOperator(
        task_id='curl',
        bash_command='echo "Hello world"'
    )
    
    load_task = BashOperator(
        task_id='load',
        bash_command='echo'
    )