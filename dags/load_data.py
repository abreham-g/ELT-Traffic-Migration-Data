
#Importing libraries
import airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.bash_operator import bash_operator
from airflow.operators.python_operator import python_operator
from airflow.operators.mysql_operator import MySqlOperator
# instantiating the Postgres Operator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

postgres_user = 'dbtuser'
postgres_password = 'pssd'
postgres_host = 'postgres-db'
postgres_db_name = 'analytics'
postgres_port = 5432


def load_to_postgres(mysql_df, table_name):
    mysql_df.columns= mysql_df.columns.str.lower()
    conn_str = f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db_name}'
    engine = create_engine(conn_str)
    mysql_df.to_sql(table_name.lower(), con=engine, index=False, if_exists='append')


default_args = {
    "owener":"airflow",
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['aynuyeabresh@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
    dag_id ="Workflow", 
    default_args=default_args,
    schedule_interval = '@daily'
    catchup=False,
    
) as dag:
create_table_sql_query = """ 
   create table if not exists open_traffic (
                id serial,
                track_id integer,
                type text,
                traveled_d numeric,
                avg_speed numeric,
                lat numeric,
                lon numeric,
                speed numeric,
                lon_acc numeric,
                lat_acc numeric,
                time numeric);
    """

create_table = PostgresOperator(
    sql = create_table_sql_query,
    task_id = "create_table_task",
    postgres_conn_id = "postgres_local",
    dag = dag_psql
    )

load_task = PythonOperator(
    task_id='load_file_to_data_lake',
    provide_context=True,
    python_callable=load_to_postgres,
    dag=dag
)

clean_task = BashOperator(
    task_id="clean_files_on_staging",
    bash_command="rm -f /tmp/*.csv;rm -f /tmp/*.json;rm -f /tmp/*.parquet;",
    dag=dag
)


 create_table >> Insert_data >>clean_task 