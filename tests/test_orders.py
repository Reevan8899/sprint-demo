import pytest

from src.orders import filter_orders_by_min_total, find_order


@pytest.fixture
def orders():
    return [{"id": "one", "total": 100, "items": [{"quantity": 1}]},
            {"id": "two", "total": 200, "items": [{"quantity": 2}]}]


def test_find_and_missing_order(orders):
    assert find_order(orders, "two")["total"] == 200
    assert find_order(orders, "absent") is None
    assert find_order([], "one") is None


def test_filter_includes_boundary(orders):
    assert [o["id"] for o in filter_orders_by_min_total(orders, 200)] == ["two"]
    assert filter_orders_by_min_total(orders, 201) == []
    assert len(filter_orders_by_min_total(orders, 0)) == 2


@pytest.mark.parametrize("minimum", [-1, 1.5, True, None])
def test_invalid_minimum(orders, minimum):
    with pytest.raises(ValueError):
        filter_orders_by_min_total(orders, minimum)


def test_results_are_independent_snapshots(orders):
    find_order(orders, "one")["items"][0]["quantity"] = 999
    filter_orders_by_min_total(orders, 0)[0]["total"] = 0
    assert orders[0]["items"][0]["quantity"] == 1
    assert orders[0]["total"] == 100
