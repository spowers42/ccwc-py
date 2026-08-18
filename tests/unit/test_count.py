import pytest
from ccwc_py.count import count_bytes, get_count_methods, count_words, count_chars


@pytest.mark.parametrize(
    "flags,num_methods",
    [
        ((False, False, False, False), 3),
        ((True, True, True, False), 3),
        ((False, True, True, False), 2),
        ((False, False, False, True), 1),
    ],
)
def test_get_count_method_exception(flags, num_methods):
    assert num_methods == len(set(get_count_methods(*flags)))


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
