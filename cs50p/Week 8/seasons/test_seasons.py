from seasons import verify
import pytest


def test_1():
    assert verify("2004-09-11")==True

def test_4():
    assert verify("1954-09-11")==True

def test_verify_exits():
    with pytest.raises(SystemExit) as exc_info:
        verify("wrong_input")
    # Optionally check the exit code or message
    assert exc_info.type == SystemExit
    assert exc_info.value.code == "no"  # the argument passed to sys.exit()

def test_verify_exits():
    with pytest.raises(SystemExit) as exc_info:
        verify("200")
    # Optionally check the exit code or message
    assert exc_info.type == SystemExit
    assert exc_info.value.code == "no"  # the argument passed to sys.exit()
