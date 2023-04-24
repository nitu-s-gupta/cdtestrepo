def print_hello():
    return 'Hello world from first Airflow DAG!'

dag = DAG('hello', description='Hello World DAG',
          schedule_interval='@hourly',
          start_date=datetime(2023, 4, 24), catchup=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello_operator
