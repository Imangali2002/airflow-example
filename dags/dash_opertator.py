from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id="bash_operator",
    default_args=default_args,
    description="Dag with bash opeartor",
    start_date=datetime(2022, 11, 7, 2),
    schedule_interval="@daily"
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the 1 task!"
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo hello world, this is the 2 task!"
    )

    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo hello world, this is the 3 task!"
    )

    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    task1 >> [task2, task3]