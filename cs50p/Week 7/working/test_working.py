from working import convert
import pytest


def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 2:45 PM") == "10:30 to 14:45"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1 PM to 3 PM") == "13:00 to 15:00"


def test_hours_off_by_one():
    # intentionally fail if output hour is off by one (simulate wrong function)
    result = convert("9:00 AM to 5:00 PM")
    assert result.startswith("09"), f"Hours off: {result}"


def test_minutes_off_by_five():
    # Make sure minutes are exact (not off by 5)
    result = convert("10:30 AM to 2:45 PM")
    assert result.endswith("14:45"), f"Minutes off: {result}"


def test_missing_to_raises():  # missing 'to'
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")  # hour 13 invalid in 12-hour time


def test_out_of_range_raises():
    with pytest.raises(ValueError):
        convert("13:00 AM to 15:00 PM")  # hour 13 invalid in 12-hour time

    with pytest.raises(ValueError):
        convert("9:61 AM to 5:00 PM")   # minute 61 invalid

    with pytest.raises(ValueError):
        convert("0:30 AM to 5:00 PM")   # hour 0 invalid in 12-hour time
