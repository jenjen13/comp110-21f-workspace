"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730404596"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
number: int = (randint(1, 100))
fortune_one: int = 25
fortune_two: int = 75
print("Your fortune cookie says...")
if fortune_one == number:
    print("This is the sign you have been waiting for. Go for it!")
else:
    if fortune_one > number:
        print("Everything will work out! Don't stress.")
    else:
        if fortune_one < number < fortune_two:
            print("You will make a new friend soon.")
        else:
            if fortune_two <= number:
                print("You have worked so hard. Keep going!")
 
 
print("Now, go spread positive vibes!")