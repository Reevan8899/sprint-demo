import pytest

from src.cart import add_to_cart, clear_cart, get_cart, total_price

PRODUCT = {"id": 1, "name": "Ноутбук", "price": 75000}


@pytest.fixture(autouse=True)
def clean_cart():
    clear_cart()
    yield
    clear_cart()


def test_add_and_combine_quantity():
    add_to_cart(PRODUCT)
    add_to_cart(PRODUCT, 2)
    assert len(get_cart()) == 1
    assert get_cart()[0]["quantity"] == 3
    assert total_price() == 225000


@pytest.mark.parametrize("quantity", [0, -1, 1.5, True, None])
def test_invalid_quantity_does_not_change_cart(quantity):
    with pytest.raises(ValueError):
        add_to_cart(PRODUCT, quantity)
    assert get_cart() == []


def test_invalid_product():
    with pytest.raises(ValueError):
        add_to_cart({"id": 1})
    assert total_price() == 0


def test_same_id_with_different_price_is_rejected():
    add_to_cart(PRODUCT)
    with pytest.raises(ValueError, match="другими данными"):
        add_to_cart({**PRODUCT, "price": 1})
    assert total_price() == 75000


def test_clear_and_empty_total():
    add_to_cart(PRODUCT)
    clear_cart()
    assert get_cart() == []
    assert total_price() == 0
