help:
	@echo "build"
	@echo "run"
	@echo "tests"

build:
	@docker build -t geoapi .

run:
	@docker run --rm geoapi:latest -v

tests:
	@pytest -v test_geoapi.py test_product_available.py test_validate_discount.py
