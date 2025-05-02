#import libraries
import pandas as pd
from airflow.operators.python import PythonOperator

def extract():
    print('yameteee')


def transform():
	pass


def load():
    pass


default_args={
     'owner': 'Cley',

}

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag,
)

extract_task >> transform_task >> load_task