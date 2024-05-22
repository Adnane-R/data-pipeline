from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'refaverama',
    'start_date': datetime(2024,3,4),
    'catchup': False
}


dag = DAG(
    'First_K8s',
    default_args = default_args,
    schedule = timedelta(days=1)
)

t1 = BashOperator(
    task_id = "first_K8s",
    bash_command = 'echo "first_k8s"',
    dag = dag
)