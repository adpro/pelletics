from datetime import datetime
from enum import Enum


class StoveEvent:
    """Event class record"""
    def __init__(self, timestamp, event_type, price=0, note=""):
        if isinstance(timestamp, datetime):
            self.timestamp = timestamp
        else:
            raise(AttributeError("Timestamp must be datetime instance"))
        if isinstance(event_type, EventType):
            self.event_type = event_type
        else:
            raise(AttributeError("Event_type must be EventType instance"))
        self.price = price
        self.note = note


class EventType(Enum):
    """Enum list of event types"""
    MAINTENANCE = 1,
    SPARE_PARTS = 2,
    FINANCING = 3,
    PAYMENT = 4,
    PURCHASE_PRICE = 5,
    MISCELLANEOUS = 6,
    ACCESSORIES = 7,
    SUPERVISORY_BOARD = 8,
    REPAIR = 9,
    ALARM = 0
