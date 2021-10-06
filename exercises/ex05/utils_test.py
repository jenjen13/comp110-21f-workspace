"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730404596"


def test_only_evens() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_sub() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_concat() -> None:
    inventory: list[int] = [1, 2, 3]
    catalog: list[int] = [4, 5, 6]
    assert concat(inventory, catalog) == [1, 2, 3, 4, 5, 6]