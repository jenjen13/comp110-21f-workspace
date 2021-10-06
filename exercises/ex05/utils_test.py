"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730404596"

"""Unit test for only_evens."""


def test_only_evens_use_case_one() -> None:
    """Test to find even numbers in a list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_use_case_two() -> None:
    """Test to find even numbers in a list."""
    xs: list[int] = [3, 4, 5, 2, 3, 1, 4]
    assert only_evens(xs) == [4, 2, 4]


def test_only_evens_edge_case() -> None:
    """If list is empty, return an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


"""Unit test for sub."""


def test_sub_use_case_one() -> None:
    """Test to create a list between two set values."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_use_case_two() -> None:
    """Test to create a list between two set values."""
    a_list: list[int] = [3, 4, 5, 6]
    assert sub(a_list, 0, 3) == [3, 4, 5]


def test_sub_edge_case() -> None:
    """If list is empty, return an empty list."""
    a_list: list[int] = []
    assert sub(a_list, 1, 3) == []


"""Unit test for concat."""


def test_concat_use_case_one() -> None:
    inventory: list[int] = [1, 2, 3]
    catalog: list[int] = [4, 5, 6]
    assert concat(inventory, catalog) == [1, 2, 3, 4, 5, 6]


def test_concat_use_case_two() -> None:
    inventory: list[int] = [20, 40, 60]
    catalog: list[int] = [10, 30, 50]
    assert concat(inventory, catalog) == [20, 40, 60, 10, 30, 50]


def test_concat_edge_case() -> None:
    inventory: list[int] = []
    catalog: list[int] = []
    assert concat(inventory, catalog) == []