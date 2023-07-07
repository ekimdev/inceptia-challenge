import pandas as pd

_PRODUCT_DF = pd.DataFrame(
    {
        "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
        "quantity": [3, 10, 0, 5],
    }
)
PRODUCTS_ATTEMPTS = {product: 0 for product in list(_PRODUCT_DF.product_name)}
INVALID_PRODUCTS_ATTEMPTS = 0
MAX_ATTEMPTS = 3


class StockError(Exception):
    pass


class ProductNotFoundError(Exception):
    pass


def check_attempts(product_name: str) -> None:
    PRODUCTS_ATTEMPTS[product_name] += 1
    product_attempts = PRODUCTS_ATTEMPTS[product_name]
    if product_attempts > MAX_ATTEMPTS:
        raise StockError(f"El producto {product_name} alcanzó el máximo de intentos")


def is_product_available(product_name: str, quantity: int, df=_PRODUCT_DF) -> bool:
    """Devuelve True si hay stock disponible. False en caso contrario.
    Levanta una excepción si el producto no existe."""
    # NOTE: Si bien query al parecer es más eficiente para DataFrame
    # con grandes cantidades de datos, para este caso opté por la sintaxis
    # de una variante del método loc que es más pythonica.
    # product = _PRODUCT_DF.query("product_name==@product_name")
    product = df[df.product_name == product_name]

    if not product.empty:
        stock_available = product["quantity"].values[0] >= quantity

        check_attempts(product_name)

        return stock_available

    raise ProductNotFoundError(f"El producto {product_name} no existe")


def main() -> None:
    # Ejemplo de uso:
    try:
        while True:
            prod, q = input(">>> ").strip().split(",")
            if is_product_available(prod, int(q)):
                print(f"Hay stock de {prod}")
                break
    except ProductNotFoundError as product_error:
        print(product_error)
    except StockError as stock_error:
        print(stock_error)


if __name__ == "__main__":
    main()
