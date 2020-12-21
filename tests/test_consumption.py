import pytest
from datetime import datetime, date
from pelletics.delivery import Delivery
from pelletics.product import Product
from pelletics.consumption import Consumption


@pytest.fixture
def sample_consumption():
    """Returns a Consumption instance with basic settings"""
    product = Product("NameA", 15, 17.85, 0.07, "oak", 0.08, "ENplusA1",
                      "Pelletics.cz", date(2020, 12, 20))
    delivery = Delivery(product, "Pellets2Home", 7350, 42500,
                        date(2020, 12, 20))
    some_datetime = datetime(2020, 11, 20, 14, 22, 46, 0)
    consumption = Consumption(some_datetime, delivery, 30, "30 kgs")
    return consumption


def test_init(sample_consumption):
    assert isinstance(sample_consumption.delivery, Delivery)
    expected_datetime = datetime(2020, 11, 20, 14, 22, 46, 0)
    assert sample_consumption.timestamp == expected_datetime
    assert sample_consumption.amount == 30
    assert sample_consumption.note == "30 kgs"
