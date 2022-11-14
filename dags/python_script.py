from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def print_hw():
    print('Hallo world')


with DAG(
    dag_id="python_script",
    default_args=default_args,
    description="DAG with python scripts",
    start_date=datetime(2022, 11, 7, 2),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="greed",
        python_callable=print_hw
    )