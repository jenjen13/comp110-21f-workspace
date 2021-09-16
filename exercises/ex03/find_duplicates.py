"""Finding duplicate letters in a word."""

__author__ = "730404596"

word: str = input("Enter a word: ")
letter: str = ""
i: int = 0
dup: str = ""
huh: str = ""

while i < (len(word)) - 1:
    letter = word[i]
    dup = word[i + 1]
    if letter == dup:
        print("true")
    print("false")
    i = i + 1
