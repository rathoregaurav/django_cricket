# Data Parsing Backend

## Environment variables
create .env file using env variables from sample env file in cricket directory


##  Project setup instruction

#### create virtual environment, 

virtualenv -p python3 venv

#### install requirement files,

pip install -r requirement/local.txt


#### run project

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 0.0.0.0:port
