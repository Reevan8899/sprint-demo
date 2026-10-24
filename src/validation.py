"""Общие правила данных: целые рубли и положительное количество."""


def require_quantity(quantity: int) -> None:
    if type(quantity) is not int or quantity <= 0:
        raise ValueError("Количество должно быть положительным целым числом")


def require_product(product: dict) -> None:
    if not isinstance(product, dict):
        raise ValueError("Товар должен быть словарём")
    if type(product.get("id")) is not int or product["id"] <= 0:
        raise ValueError("ID товара должен быть положительным целым числом")
    name = product.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Название товара обязательно")
    if type(product.get("price")) is not int or product["price"] < 0:
        raise ValueError("Цена должна быть неотрицательным целым числом рублей")
