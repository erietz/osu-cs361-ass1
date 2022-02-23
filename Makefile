.PHONY: serve
serve:
	uvicorn plotz.main:app --reload

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: requirements
requirements:
	pipreqs . --force

.PHONY: install
test:
	python -m pytest
