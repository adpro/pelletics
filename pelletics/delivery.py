from datetime import date
from pelletics.product import Product


class Delivery:
    """Delivery record class"""
    def __init__(self, product, supplier, amount, price,
                 curr_date):
        if isinstance(product, Product):
            self.product = product
        else:
            raise(AttributeError(
                    "Product must be pelletics.product.Product instance"))
        self.supplier = supplier
        self.weight = amount    # in kgs or lbs
        self.price = price  # in selected currency
        if isinstance(curr_date, date):
            self.date = curr_date
        else:
            raise(AttributeError("Date must be datetime.date instance"))
