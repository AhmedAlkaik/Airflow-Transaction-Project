from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime,timedelta
from pipeline_start_timestamp import trans_start_time
from trans_report import trans_report_gen


default_args = {
    'owner' : 'airflow',
    'start_date': datetime(2026,4,13),
}


with DAG(
    dag_id = 'transaction_processing',
    default_args = default_args,
    schedule_interval =  timedelta(minutes=10),
    catchup = False
) as dag:

    task_1 = PythonOperator(
        task_id = 'pipeline_start_timestamp',
        python_callable = trans_start_time
    )

    task_2 = PythonOperator(
        task_id = 'trans_report',
        python_callable = trans_report_gen
    )

    task_3 = BashOperator(
        task_id = 'run_process_transactions_script',
        bash_command = 'python /data/process_transactions.py && cat /data/transactions_report.txt'
    )
    
    task_4 = EmailOperator(
        task_id = 'Report_email',
        to = 'ahmedalkaik04@gmail.com',
        subject = 'Transaction Report',
        html_content = task_3.output 
        )
    task_1 >> task_2 >> task_3 >> task_4