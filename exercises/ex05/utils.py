"""List utility functions part 2."""

__author__ = "730404596"

# Define your functions below


def only_evens(record: list[int]) -> list[int]:
    """Find the even numbers within a list."""
    i: int = 0
    another: list[int] = []
    while i < len(record):
        if record[i] % 2 == 0:
            another.append(record[i])
        i += 1
    return another


def sub(a_list: list[int], figure: int, character: int) -> list[int]:
    """Create a list in between two values from a list."""
    i: int = 0
    addition: list[int] = []
    while i < len(a_list):
        while figure <= i < character:
            addition.append(a_list[i])
            i += 1
        i += 1
    return addition
        
        
def concat(inventory: list[int], catalog: list[int]) -> list[int]:
    """Print the first list and then the second."""
    number: list[int] = []
    i: int = 0
    while i < len(inventory):
        number.append(inventory[i])
        i += 1

    i = 0
    while i < len(catalog):
        number.append(catalog[i])
        i += 1
    return number