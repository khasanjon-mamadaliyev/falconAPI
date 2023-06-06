make:
	python3 manage.py makemigrations
mig:
	python3 manage.py migrate

admin:
	python manage.py createsuperuser --email admin@gmail.com