"""Finding duplicate letters in a word."""

__author__ = "730404596"

word: str = input("Enter a word: ")
letter: str = ""
i: int = 0
g: int = 0

while i < (len(word)):
    letter = word[i]
    g = i + 1
    while g < (len(word)): 
        if letter == word[g]:
            print("Found duplicate: True")
        else:
            print("Found duplicate: False")
        g = g + 1
    i = i + 1
