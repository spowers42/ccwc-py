import pytest
from ccwc_py.count import count_bytes, get_count_method, count_words, count_chars


def test_get_count_method_exception():
    with pytest.raises(NotImplementedError):
        get_count_method(False, False, False, False)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("test test", 9),
        ("🤗", 4),
    ],
)
def test_count_bytes(text: str, expected: int):
    count = count_bytes(text)
    assert count == expected


@pytest.mark.parametrize(
    "text,expected", [("a b c d e", 5), ("🦎 🦎 🦎 🦎 🦎", 5), ("🦎🦎🦎🦎🦎", 1)]
)
def test_count_words(text, expected):
    count = count_words(text)
    assert count == expected


@pytest.mark.parametrize(
    "text,expected", [("abcdefg", 7), ("🦎 🦎 🦎 🦎 🦎", 9), ("🦎🦎🦎🦎🦎", 5)]
)
def test_character_count(text, expected):
    count = count_chars(text)
    assert count == expected
