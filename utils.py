import json
from typing import List


def read_file(path: str):
    with open(path, 'r') as json_file:
        return json.load(json_file)


def capitalize(value: str) -> str:
    return value[0].upper() + value[1:]


def pluck(source: dict, args: list) -> List[str]:
    return [str(source[arg]) if arg in source else "" for arg in args]


def is_match(source, other) -> bool:
    return str(source).lower() == str(other).lower()


def search_text(
        source: str,
        pattern: [int, str, bool, list],
        is_strict: bool = False
) -> bool:
    if type(pattern) is bool or type(pattern) is int or is_strict is True:
        return is_match(source, pattern)
    elif not source:
        return is_match(source, str(pattern).strip())
    else:
        return source in pattern
