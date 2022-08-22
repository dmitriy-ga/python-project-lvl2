install:
	poetry install

gendiff-run-test:
	poetry run pytest gendiff

build:
	poetry build

lint:
	poetry run flake8 gendiff