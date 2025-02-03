from lib.counter import *


def test_add_12_then_add_5_more():
    counter = Counter()
    counter.add(12)
    result = counter.report()
    counter.add(5)
    result2 = counter.report()
    assert result == "Counted to 12 so far"
    assert result2 == "Counted to 17 so far"
