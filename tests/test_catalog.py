import pytest

from src.catalog import get_product, list_products


def test_list_contains_three_products():
    products = list_products()
    assert [p["id"] for p in products] == [1, 2, 3]
    assert all(p["price"] >= 0 for p in products)


def test_get_product_by_id():
    assert get_product(2) == {"id": 2, "name": "Мышь", "price": 1500}


@pytest.mark.parametrize("product_id", [0, 999, True, "1", None])
def test_unknown_or_invalid_id(product_id):
    with pytest.raises(KeyError):
        get_product(product_id)



def test_returned_products_cannot_mutate_catalog():
    products = list_products()
    products[0]["price"] = 1
    get_product(1)["name"] = "Подмена"
    assert get_product(1)["price"] == 75000
    assert get_product(1)["name"] == "Ноутбук"
