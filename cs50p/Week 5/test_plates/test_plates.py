from plates import is_valid


def test1():
    assert is_valid("33302") == False  # Invalid plate (Starts with numbers, violates letter rule)


def test2():
    # Valid plate (Starts with a letter, alphanumeric, numbers at the end)
    assert is_valid("HB420") == True


def test3():
    assert is_valid("He0L0") == False  # Invalid plate (Zero placed within the number section)


def test4():
    assert is_valid("") == False  # Invalid plate (Empty string)


def test5():
    # Valid plate (Starts with a letter, alphanumeric, numbers at the end)
    assert is_valid("ABC123") == True


def test6():
    assert is_valid("AB1234567") == False  # Invalid plate (Too long)


def test7():
    assert is_valid("AB012") == False  # Invalid plate (Zero placed at the start of number)


def test8():
    assert is_valid("AB12*") == False  # Invalid plate (Contains special character)


def test9():
    assert is_valid("1ABC123") == False  # Invalid plate (Starts with a number)


def test10():
    assert is_valid("A") == False  # Invalid plate (Too short)


def test11():
    assert is_valid("AB12A") == False  # Invalid plate (Alphabet after number)
