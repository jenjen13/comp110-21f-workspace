"""List utility functions."""

__author__ = "730404596"


# TODO: Implement your functions here.

def all(ex: list[int], lol: int) -> bool:
    """Find ints."""
    i: int = 0 
    while i < (len(ex)):
        if ex[i] != lol:
            return False
        i += 1
    return True


def is_equal(ki: list[int], bo: list[int]) -> bool:
    """Given two lists of ints, return True if every elemtn is equal."""
    if ki != bo:
        return False
    return True


def max(lop: list[int]) -> int:
    """Given a list of ints, max should return the largest in list."""
    i: int = 0
    if len(lop) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        while i < len(lop):
            if lop[i] > lop[i - 1]:
                return lop[i]
            i += 1
    return lop[i]