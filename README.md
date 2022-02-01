# restaurant-api

## Requirements

- Docker 20.10.11

## Setup

Before you start, setup the `.env` file. You can simply compy the available example:

```shell script
cp .env.sample .env
```

First of all, build the project image:

```shell script
make build
```

Then, to run the server:

```shell script
make run
```

And to run the database migrations:

```shell script
make migrate
```

To run the tests:

```shell script
make test
```
