build:
	docker compose build

migrate:
	./run.sh python manage.py migrate

run:
	./run.sh python manage.py runserver 0.0.0.0:8000

test:
	./run.sh pytest -s --maxfail=1
