# Test task project - debt approval api
## Entities:
- DebtRequest
- Contract
- Item
- Manufacturer

## Requirement:
Create an API to get unique manufacturer ids using a given contract.

## Initial setup

##### Install Poetry

Follow the official [Poetry Installation Manual](https://python-poetry.org/docs/#installation).

##### Set local Python version

Follow the official [Pyenv Installation Manual](https://github.com/pyenv/pyenv#installation).

```shell
pyenv local <python version>
```

##### Set up virtual environment

```shell
poetry env use $(pyenv which python)
```

##### Install dependencies

```shell
poetry install
```

## Dev info

##### Setup local DB

Run database migration:

```shell
python manage.py migrate
```

##### Start the application locally

Run the application:

```shell
python backend/manage.py runserver
```

## Test the application locally with seeded data

Seed the DB:

```shell
python backend/manage.py seed_db
```

Navigate to the browser to test the endpoint:
http://127.0.0.1:8000/debt_approval_api/manufacturers/1/

## Manage Docker containers

Build and run the container locally:

```shell
docker-compose up --build
```


