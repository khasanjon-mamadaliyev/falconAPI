web: gunicorn root.wsgi:application
release: python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py collectstatic --noinput
worker: celery -A root worker -P gevent -l info
