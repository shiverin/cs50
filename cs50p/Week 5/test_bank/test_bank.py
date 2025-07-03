from bank import value


def test1():
    assert value("yo") == 100


def test2():
    assert value("Hey") == 20


def test3():
    assert value("HeLLo") == 0


def test4():
    assert value("123!@#") == 100
