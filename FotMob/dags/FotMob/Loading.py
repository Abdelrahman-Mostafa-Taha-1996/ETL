import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.hooks.base import BaseHook
print(BaseHook.get_hook('FotMob_conn'))

def generate_insert_sql(table_name, data, columns):
    columns_str = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(columns))

    sql = f"INSERT INTO fotmob.{table_name} ({columns_str}) VALUES ({placeholders})"
    values = [tuple(row[col] for col in columns) for row in data]

    return sql, values

def insert_data(**kwargs):
    table_name = kwargs['table_name']
    key = kwargs['key']
    matches_data = kwargs['ti'].xcom_pull(task_ids='fetch_data', key=key)
    matches_df = pd.DataFrame(matches_data).drop_duplicates()
    print(matches_df.head())
    matches_insert_sql, matches_values = generate_insert_sql(table_name, matches_df.to_dict(orient='records'), matches_df.columns)

    hook = PostgresHook(postgres_conn_id = 'FotMob_conn')
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.executemany(matches_insert_sql, matches_values)
    conn.commit()
    cursor.close()
    conn.close()
    return "Matches data inserted successfully"