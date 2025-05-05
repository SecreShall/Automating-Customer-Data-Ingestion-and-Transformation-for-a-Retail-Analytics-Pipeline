#import libraries
from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import timedelta
import ETL




default_args={
     'owner': 'Cley',
}

dag = DAG(
     dag_id='retail_etl',
     default_args=default_args,
     description='Retail Analytics Pipeline',
     schedule=timedelta(days=1),
)

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