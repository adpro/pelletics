import pytest
from datetime import date
from pelletics.product import Product


@pytest.fixture
def sample_product():
    """Returns a Product instance with basic settings"""
    return Product("NameA", 15, 0.07, "oak", 0.08, "ENplusA1",
                   date(2020, 12, 20))


def test_init(sample_product):
    """Test constructor of Product class"""
    assert sample_product.name == "NameA"
    assert sample_product.bag_size == 15
    assert sample_product.moisture == 0.07
    assert sample_product.raw_material == "oak"
    assert sample_product.ash_pct == 0.08
    assert sample_product.standard == "ENplusA1"
    assert sample_product.date == date(2020, 12, 20)


@pytest.mark.xfail(raises=AttributeError)
def test_init_wrong_data_type():
    """Initialize Product instance with wrong date type"""
    Product("NameA", 15, 0.07, "oak", 0.08, "ENplusA2",
            "2020-12-20")


def test_str(sample_product):
    """Test __str__ of Product class"""
    assert str(sample_product) == "NameA 12-2020"
