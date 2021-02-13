install:
	@poetry install

build: check
	@poetry build

test:
	@poetry run pytest --cov-report term --cov-report xml --cov=page_loader page_loader tests

lint:
	@poetry run flake8 page_loader tests