web: gunicorn root.wsgi
release: python3 manage.py migrate --no-input && python3 manage.py collectstatic --no-input