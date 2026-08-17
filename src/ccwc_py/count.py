from collections.abc import Callable


def get_count_method(
    count_bytes_flag: bool,
    count_lines_flag: bool,
    count_words_flag: bool,
    count_chars_flag: bool,
) -> Callable[[str], int]:
    if count_bytes_flag:
        return count_bytes
    if count_lines_flag:
        return count_lines
    if count_words_flag:
        return count_words
    if count_chars_flag:
        return count_chars
    raise NotImplementedError("no available count method")


def count_bytes(text: str) -> int:
    text = text.encode("utf-8")
    return len(text)


def count_lines(text: str) -> int:
    return 1


def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> int:
    return len(text)
