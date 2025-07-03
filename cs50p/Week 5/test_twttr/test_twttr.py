from twttr import shorten


def test_lowercase_vowels():
    assert shorten("hello") == "hll"


def test_uppercase_vowels():
    assert shorten("HELLO") == "HLL"


def test_mixed_case():
    assert shorten("HeLLo") == "HLL"


def test_numbers_and_punctuation():
    assert shorten("123!@#") == "123!@#"
