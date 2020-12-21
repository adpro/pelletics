import datetime
from pelletics.delivery import Delivery


class Consumption:
    """Consumption record class"""
    def __init__(self, curr_datetime, delivery, amount, note):
        if isinstance(curr_datetime, datetime.datetime):
            self.timestamp = curr_datetime
        else:
            raise(AttributeError(
                "Curr_datetime must be datetime.datetime instance"))
        if isinstance(delivery, Delivery):
            self.delivery = delivery
        else:
            raise(AttributeError("Delivery must be Delivery instance"))
        if amount > 0:
            self.amount = amount
        else:
            raise(AttributeError("Amount must be bigger than zero"))
        self.note = note
