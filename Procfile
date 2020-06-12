release:python manage.py makemigrations,
        python manage.py migrate
web: gunicorn project_name.wsgi
python manage.py runserver 0.0.0.0:$PORT