release:python manage.py makemigrations,
        python manage.py migrate
web: gunicorn messagesapi.wsgi
python manage.py runserver 0.0.0.0:$PORT