import pytest
from jar import Jar


def test_init_and_str():
    jar = Jar(12)
    assert jar.capacity == 12
    assert jar.size == 0
    assert str(jar) == ""  # empty jar prints empty string


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪" * 5


def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size == 4


def test_deposit_over_capacity_raises():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw_too_much_raises():
    jar = Jar(5)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(4)


def test_negative_capacity_raises():
    with pytest.raises(ValueError):
        Jar(-1)
