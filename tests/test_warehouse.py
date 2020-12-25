import pytest
# from datetime import datetime, date
# from pelletics.delivery import Delivery
# from pelletics.product import Product
# from pelletics.consumption import Consumption
from pelletics.warehouse import Warehouse


@pytest.fixture
def empty_warehouse():
    """Return empty warehouse"""
    return Warehouse()

# @pytest.fixture
# def sample_consumption():
#     """Returns a Consumption instance with basic settings"""
#     product = Product("NameA", 15, 17.85, 0.07, "oak", 0.08, "ENplusA1",
#                       "Pelletics.cz", date(2020, 12, 20))
#     delivery = Delivery(product, "Pellets2Home", 7350, 42500,
#                         date(2020, 12, 20))
#     some_datetime = datetime(2020, 11, 20, 14, 22, 46, 0)
#     consumption = Consumption(some_datetime, delivery, 30, "30 kgs")
#     return consumption


def test_init_empty(empty_warehouse):
    assert empty_warehouse.fullness == 0
    assert empty_warehouse.max_fullness == 0
    assert isinstance(empty_warehouse.deliveries, list)
    assert len(empty_warehouse.deliveries) == 0
    assert isinstance(empty_warehouse.consumptions, list)
    assert len(empty_warehouse.consumptions) == 0
    assert isinstance(empty_warehouse.events, list)
    assert len(empty_warehouse.events) == 0
