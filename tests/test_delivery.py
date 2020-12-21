import pytest
from datetime import date
from pelletics.delivery import Delivery
from pelletics.product import Product


@pytest.fixture
def sample_delivery():
    """Returns a Delivery instance with basic settings"""
    product = Product("NameA", 15, 17.85, 0.07, "oak", 0.08, "ENplusA1",
                      "Pelletics.cz", date(2020, 12, 20))
    delivery = Delivery(product, "Pellets2Home", 7350, 42500,
                        date(2020, 12, 20))
    return delivery


def test_init(sample_delivery):
    """Test constructor of Delivery class"""
    assert isinstance(sample_delivery.product, Product)
    assert sample_delivery.product.name == "NameA"
    assert sample_delivery.supplier == "Pellets2Home"
    assert sample_delivery.weight == 7350
    assert sample_delivery.price == 42500
    assert sample_delivery.date == date(2020, 12, 20)
    assert sample_delivery.rest_amount == 7350


def test_init_wrong_data_type():
    """Initialize Product instance with wrong date type"""
    with pytest.raises(AttributeError):
        Product("NameA", 15, 17.85, 0.07, "oak", 0.08, "ENplusA2",
                "Pelletics.cz", "2020-12-20")
