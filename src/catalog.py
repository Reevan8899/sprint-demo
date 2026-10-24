"""Каталог: наружу возвращаются копии, цены заданы в целых рублях."""
from copy import deepcopy

_products = [
    {"id": 1, "name": "Ноутбук", "price": 75000},
    {"id": 2, "name": "Мышь", "price": 1500},
    {"id": 3, "name": "Клавиатура", "price": 3500},
]


def list_products() -> list[dict]:
    """Вернуть снимок каталога."""
    return deepcopy(_products)


def get_product(product_id: int) -> dict:
    """Найти товар; неизвестный ID вызывает KeyError."""
    if type(product_id) is int:
        for product in _products:
            if product["id"] == product_id:
                return deepcopy(product)
    raise KeyError(f"Товар с id={product_id} не найден")
