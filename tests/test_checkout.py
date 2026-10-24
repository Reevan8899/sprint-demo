import pytest

from src.checkout import clear_orders, create_order, get_orders


@pytest.fixture(autouse=True)
def clean_orders():
    clear_orders()
    yield
    clear_orders()


@pytest.fixture
def cart():
    return [{"product": {"id": 2, "name": "Мышь", "price": 1500}, "quantity": 2}]


def test_order_total_and_unique_id(cart):
    order = create_order(cart, "Учебный адрес, 1")
    another = create_order(cart, "Учебный адрес, 2")
    assert order["total"] == 3000
    assert order["id"] != another["id"]
    assert len(get_orders()) == 2


@pytest.mark.parametrize("cart", [[], None, [None], [{}],
    [{"product": {"id": 1}, "quantity": 1}],
    [{"product": {"id": 1, "name": "Товар", "price": 100}, "quantity": -1}]])
def test_invalid_cart_does_not_create_order(cart):
    with pytest.raises(ValueError):
        create_order(cart, "Учебный адрес, 1")
    assert get_orders() == []


def test_order_is_snapshot_of_cart(cart):
    order = create_order(cart, "Учебный адрес, 1")
    cart[0]["product"]["price"] = 1
    order["items"][0]["quantity"] = 999
    snapshot = get_orders()
    snapshot[0]["address"] = "Подмена"
    stored = get_orders()[0]
    assert stored["total"] == 3000
    assert stored["items"][0]["product"]["price"] == 1500
    assert stored["items"][0]["quantity"] == 2
    assert stored["address"] == "Учебный адрес, 1"



@pytest.mark.parametrize("address", ["", "   ", None])
def test_invalid_address_does_not_create_order(cart, address):
    with pytest.raises(ValueError, match="Адрес"):
        create_order(cart, address)
    assert get_orders() == []


def test_address_is_trimmed(cart):
    assert create_order(cart, "  Учебный адрес, 1  ")["address"] == "Учебный адрес, 1"
