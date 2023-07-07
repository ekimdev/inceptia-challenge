from validate_discount import validate_discount_code


def test_validate_return_true():
    assert validate_discount_code("primavera2021")


def test_assert_not_true_by_passing_validation_discount_code():
    assert not validate_discount_code("codigo_descuento")
