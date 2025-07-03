import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("0/4") == 0
    assert convert("1/100") == 1


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")  # Invalid format
    with pytest.raises(ValueError):
        convert("3/2")      # Numerator > denominator


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
