from collections.abc import Callable


def get_count_method(count_bytes_flag: bool) -> Callable[[str], int]:
    if count_bytes_flag:
        return count_bytes
    raise NotImplementedError("no available count method")


def count_bytes(text: str) -> int:
    text = text.encode("utf-8")
    return len(text)
