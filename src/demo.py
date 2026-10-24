"""Живая демонстрация Sprint Goal: python -m src.demo."""
from src.auth import login, register, reset_users
from src.cart import add_to_cart, clear_cart, get_cart, total_price
from src.catalog import get_product, list_products
from src.checkout import clear_orders, create_order, get_orders
from src.orders import filter_orders_by_min_total, find_order


def main() -> None:
    reset_users()
    clear_cart()
    clear_orders()
    register("student@example.com", "demo-pass-2026")
    print("1. Вход:", login("student@example.com", "demo-pass-2026"))
    print("2. Товаров в каталоге:", len(list_products()))
    add_to_cart(get_product(1))
    add_to_cart(get_product(2), 2)
    print("3. Сумма корзины:", total_price(), "руб.")
    order = create_order(get_cart(), "Учебный адрес, дом 1")
    clear_cart()
    print("4. Заказ оформлен:", order["total"], "руб.")
    print("5. Заказ найден в истории:", find_order(get_orders(), order["id"]) is not None)
    print("6. Заказов от 50000 руб.:", len(filter_orders_by_min_total(get_orders(), 50000)))
    print("7. Корзина после оформления:", get_cart())


if __name__ == "__main__":
    main()
