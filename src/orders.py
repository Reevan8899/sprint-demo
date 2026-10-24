"""Поиск и фильтрация переданной истории заказов."""
from copy import deepcopy


def find_order(orders: list[dict], order_id: str) -> dict | None:
    for order in orders:
        if order["id"] == order_id:
            return deepcopy(order)
    return None


def filter_orders_by_min_total(orders: list[dict], min_total: int) -> list[dict]:
    if type(min_total) is not int or min_total < 0:
        raise ValueError("Минимальная сумма должна быть неотрицательным целым числом")
    return deepcopy([order for order in orders if order["total"] >= min_total])
