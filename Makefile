help:
	@echo "build"
	@echo "tests"

build:
	@docker build -t geoapi .

tests:
	@pytest -v test_geoapi.py test_product_available.py test_validate_discount.py
