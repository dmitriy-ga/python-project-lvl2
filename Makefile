install:
	poetry install

gendiff-run-flat-test:
	poetry run python3 gendiff/scripts/gendiff_start.py gendiff/file1.json gendiff/file2.json

build:
	poetry build