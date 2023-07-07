import pandas as pd
import pytest

from product_available import StockError, is_product_available, ProductNotFoundError
import product_available


def test_product_not_exist():
    df = pd.DataFrame({"product_name": ["Menta", "Caramelo"], "quantity": [3, 0]})
    product_name = "Vainilla"

    with pytest.raises(ProductNotFoundError):
        is_product_available(product_name, 3, df=df)


@pytest.mark.parametrize(
    "product_name, quantity, expected",
    [("Maracuya", 3, True), ("Menta", 4, False), ("Caramelo", 1, None)],
)
def test_is_product_available(product_name, quantity, expected):
    df = pd.DataFrame(
        {"product_name": ["Menta", "Caramelo", "Maracuya"], "quantity": [3, 0, 4]}
    )
    # HACK: esto es necesario para cambiar el valor de la variable global
    product_available.PRODUCTS_ATTEMPTS = {
        product: 0 for product in list(df.product_name)
    }

    if expected is None:
        is_product_available(product_name, quantity, df=df)
        is_product_available(product_name, quantity, df=df)
        is_product_available(product_name, quantity, df=df)
        with pytest.raises(StockError):
            is_product_available(product_name, quantity, df=df)
    else:
        is_available = is_product_available(product_name, quantity, df)

        assert is_available == expected
