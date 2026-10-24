"""Создание и хранение снимков заказов в памяти процесса."""
from copy import deepcopy
from uuid import uuid4

from src.validation import require_product, require_quantity

_orders: list[dict] = []


def create_order(cart: list[dict], address: str) -> dict:
    """Создать заказ из валидной непустой корзины; вернуть независимую копию."""
    if not isinstance(cart, list) or not cart:
        raise ValueError("Корзина пуста или имеет неверный формат")
    if not isinstance(address, str) or not address.strip():
        raise ValueError("Адрес доставки обязателен")
    for item in cart:
        if not isinstance(item, dict) or "product" not in item or "quantity" not in item:
            raise ValueError("Некорректная позиция корзины")
        require_product(item["product"])
        require_quantity(item["quantity"])
    order = {
        "id": str(uuid4()),
        "items": deepcopy(cart),
        "address": address.strip(),
        "total": sum(i["product"]["price"] * i["quantity"] for i in cart),
    }
    _orders.append(order)
    return deepcopy(order)


def get_orders() -> list[dict]:
    return deepcopy(_orders)


def clear_orders() -> None:
    _orders.clear()
