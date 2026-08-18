from collections.abc import Callable


def get_count_methods(
    count_bytes_flag: bool,
    count_lines_flag: bool,
    count_words_flag: bool,
    count_chars_flag: bool,
) -> list[Callable[[str], int]]:
    count_methods = []
    if count_lines_flag:
        count_methods.append(count_lines)
    if count_words_flag:
        count_methods.append(count_words)
    if count_bytes_flag:
        count_methods.append(count_bytes)
    if count_chars_flag:
        count_methods.append(count_chars)
    return count_methods if count_methods else [count_lines, count_words, count_bytes]


def count_bytes(text: str) -> int:
    text = text.encode("utf-8")
    return len(text)


def count_lines(text: str) -> int:
    return 1


def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> int:
    return len(text)
