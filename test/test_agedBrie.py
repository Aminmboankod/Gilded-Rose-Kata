from src.main import *
import pytest

@pytest.fixture
def store():
    item = AgedBrie("Aged Brie", 2, 0)
    return item

@pytest.mark.agedBrie
def test_agedBrie(store):

    for day in range(3):
        print("-------------- Day: %s -----------------" % (day))
        store.updateQuality()
        print(store.__repr__())