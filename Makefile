build:
	docker compose build

migrate:
	./run.sh python manage.py migrate

run:
	./run.sh python manage.py runserver
