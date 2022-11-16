source venv/bin/activate

1. install airflow with pip from github
2. export AIRFLOW_HOME="$PWD"
3. airflow db init
4. load_example=False
5. airflow users create --username airflow --password airflow --firstname firstname --lastname lastname --role Admin --email admin@domain.com
6. airflow db reset, airflow db init
7. airflow webserver -p 8080
8. airflow scheduler
