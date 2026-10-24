import pytest

from src.auth import login, register, reset_users
from src.cart import add_to_cart, clear_cart, get_cart, total_price
from src.catalog import get_product
from src.checkout import clear_orders, create_order, get_orders
from src.orders import filter_orders_by_min_total, find_order


@pytest.fixture(autouse=True)
def clean_state():
    reset_users()
    clear_cart()
    clear_orders()
    yield
    reset_users()
    clear_cart()
    clear_orders()


def test_full_purchase_and_history_survive_cart_cleanup():
    assert register("student@example.com", "demo-pass-2026")
    assert login("student@example.com", "demo-pass-2026")
    add_to_cart(get_product(1))
    add_to_cart(get_product(2), 2)
    assert total_price() == 78000
    order = create_order(get_cart(), "Учебный адрес, 1")
    clear_cart()
    stored = find_order(get_orders(), order["id"])
    assert stored["total"] == 78000
    assert len(stored["items"]) == 2
    assert get_cart() == []
    assert filter_orders_by_min_total(get_orders(), 78000) == [stored]


def test_failed_checkout_preserves_cart_and_does_not_create_order():
    add_to_cart(get_product(3))
    with pytest.raises(ValueError, match="Адрес"):
        create_order(get_cart(), "   ")
    assert total_price() == 3500
    assert get_orders() == []
