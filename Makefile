# Formating and linting code
.PHONY: refactor
refactor:
	@poetry run black .
	@poetry run mypy .

# Run project
.PHONY: run
run:
	@poetry run python -B -m $(shell poetry version | awk '{print $1}')