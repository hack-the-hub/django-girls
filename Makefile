.PHONY: runserver

runserver:
	cd volman && python manage.py runserver 0.0.0.0:8000

shell:
	cd volman && python manage.py shell

makemigrations:
	cd volman && python manage.py makemigrations

migrate:
	cd volman && python manage.py migrate
