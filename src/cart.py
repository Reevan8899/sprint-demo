"""Корзина с проверкой товаров и количества."""
from copy import deepcopy

from src.validation import require_product, require_quantity

_cart: list[dict] = []


def add_to_cart(product: dict, quantity: int = 1) -> None:
    require_product(product)
    require_quantity(quantity)
    for item in _cart:
        if item["product"]["id"] == product["id"]:
            if item["product"] != product:
                raise ValueError("Товар с этим ID уже добавлен с другими данными")
            item["quantity"] += quantity
            return
    _cart.append({"product": deepcopy(product), "quantity": quantity})


def get_cart() -> list[dict]:
    """Вернуть независимый снимок корзины."""
    return deepcopy(_cart)


def clear_cart() -> None:
    _cart.clear()


def total_price() -> int:
    return sum(item["product"]["price"] * item["quantity"] for item in _cart)
