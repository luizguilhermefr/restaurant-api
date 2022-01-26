# restaurant-api

## Setup

First of all, build the project image:

```shell script
docker compose build
```

Then run the migrations:

```shell script
./run.sh python manage.py migrate
```

To run the server:

```shell script
./run.sh python manage.py runserver
```
