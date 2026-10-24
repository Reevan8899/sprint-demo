import pytest

from src.validation import require_product, require_quantity


@pytest.mark.parametrize("quantity", [0, -1, 1.5, True, None, "2"])
def test_reject_invalid_quantity(quantity):
    with pytest.raises(ValueError):
        require_quantity(quantity)


def test_accept_positive_integer_quantity():
    require_quantity(2)


@pytest.mark.parametrize("product", [None, {}, {"id": True},
    {"id": 1, "name": " ", "price": 0},
    {"id": 1, "name": "Товар", "price": -1},
    {"id": 1, "name": "Товар", "price": float("nan")}])
def test_reject_invalid_product(product):
    with pytest.raises(ValueError):
        require_product(product)


def test_free_product_is_valid():
    require_product({"id": 1, "name": "Подарок", "price": 0})
