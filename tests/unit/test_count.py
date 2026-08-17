import pytest
from ccwc_py.count import count_bytes, get_count_method


def test_get_count_method_exception():
    with pytest.raises(NotImplementedError):
        get_count_method(False)


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
