install:
	@poetry install

build: check
	@poetry build

test:
	poetry run pytest -v

lint:
	poetry run flake8 page_loader tests

coverage:
	poetry run pytest --cov=page_loader --cov-report xml