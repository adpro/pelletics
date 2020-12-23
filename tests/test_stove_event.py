import pytest
from datetime import datetime
from pelletics.stove_event import StoveEvent, EventType


@pytest.fixture
def sample_event():
    return StoveEvent(datetime(2020, 12, 20, 14, 58, 23, 0),
                      EventType.ALARM,
                      3,
                      "Note A")


def test_init(sample_event):
    assert sample_event.timestamp == datetime(2020, 12, 20, 14, 58, 23, 0)
    assert sample_event.timestamp.day == 20
    assert sample_event.event_type == EventType.ALARM
    assert sample_event.price == 3
    assert sample_event.note == "Note A"
