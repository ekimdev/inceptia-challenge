_AVAILABLE_DISCOUNT_CODES = [
    "Primavera2021",
    "Verano2021",
    "Navidad2x1",
    "heladoFrozen",
]


def validate_discount_code(discount_code: str) -> bool | None:
    """
    Ejemplo:
    "primavera2021" deberia devolver True, ya que al compararlo:
    vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
    vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o',
    'm', 'V', 'p', 'v')
    vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0',
    'x', 'e', 'd', 'p', 'r')
    vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i',
    'v', 'n',
    'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
    """
    # FIXME: esta función produce un bucle infinito al retornar False.
    # al igual que el ejercicio 2.1.
    max_chars = 3

    for code in _AVAILABLE_DISCOUNT_CODES:
        return len(set(code).symmetric_difference(discount_code)) < max_chars


def main() -> None:
    # Ejemplo de uso:
    while True:
        discount_code = input("Ingresa un código de descuento: ")
        if validate_discount_code(discount_code):
            print("Código valido!")
            break


if __name__ == "__main__":
    main()
