from airflow import DAG
from FotMob.Extract import fetch_and_process_data
from FotMob.Loading import insert_data
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'FotMob',
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='fotmob_dag',
    default_args=default_args,
    schedule_interval='@once',
    description='Load italian football past seasons into PostgreSQL',
    tags=['Seria-A', 'football_data'],
    template_searchpath=['./plugins']
) as dag:
    fetch_data_task = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_and_process_data,
        provide_context=True
    )

    create_db_table_task=PostgresOperator(
        task_id='create_db_tables',
        postgres_conn_id='FotMob_conn',
        sql='FotMob/create_tables.sql'
    )

    # Task to load matches data into database
    insert_matches_data_task = PythonOperator(
        task_id='insert_matches_data',
        python_callable=insert_data,
        op_kwargs={'table_name': 'matches', 'key': 'matches_data'}
    )

    # Task to load teams data into database
    insert_teams_data_task = PythonOperator(
        task_id='insert_teams_data',
        python_callable=insert_data,
        op_kwargs={'table_name': 'teams', 'key': 'teams_data'}
    )
  
    # Task to load standing data into database  
    insert_standings_data_task = PythonOperator(
        task_id='insert_standings_data',
        python_callable=insert_data,
        op_kwargs={'table_name': 'standings', 'key': 'standings_data'}
    )

fetch_data_task >> create_db_table_task >> insert_teams_data_task >> [insert_matches_data_task, insert_standings_data_task]