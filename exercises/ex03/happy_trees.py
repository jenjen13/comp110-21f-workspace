"""Drawing forests in a loop."""

__author__ = "730404596"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
second: str = str()
counter: int = 0


while counter < depth:
    second = second + TREE 
    print(second)
    counter = counter + 1