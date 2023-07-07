import pandas as pd

_PRODUCT_DF = pd.DataFrame(
    {
        "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
        "quantity": [3, 10, 0, 5]
    })
PRODUCTS_ATTEMPTS = {product: 0 for product in list(_PRODUCT_DF.product_name)}
INVALID_PRODUCTS_ATTEMPTS = 0
MAX_ATTEMPTS = 3


class StockError(Exception):
    pass


class ProductNotFoundError(Exception):
    pass


def check_attempts(product_name: str):
    PRODUCTS_ATTEMPTS[product_name] += 1
    product_attempts = PRODUCTS_ATTEMPTS[product_name]
    if product_attempts > MAX_ATTEMPTS:
        raise StockError(f"El producto {product_name} alcanzó el máximo de intentos")


def is_product_available(product_name: str, quantity: int, df=_PRODUCT_DF) -> bool:
    # NOTE: si bien query al parecer es mas eficiente para DataFrame con grandes
    # cantidades de datos, para este caso opte por la sintaxis de una variante del metodo loc que es mas pythonica.
    # product = _PRODUCT_DF.query("product_name==@product_name")
    product = df[df.product_name == product_name]

    if not product.empty:
        stock_available = product["quantity"].values[0] >= quantity

        check_attempts(product_name)

        return stock_available

    raise ProductNotFoundError(f"El producto {product_name} no existe")


def main() -> None:
    print(is_product_available("Chocolate", 4))
    print(is_product_available("Chocolate", 3))
    print(is_product_available("chocolate", 2))


if __name__ == "__main__":
    main()
