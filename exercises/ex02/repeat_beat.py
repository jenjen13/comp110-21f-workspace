"""Repeating a beat in a loop."""

__author__ = "730404596"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
counter: int = 0
maximum: int = int(input("How many times do you want to repeat it? "))
second: str = str()
if maximum < 1:
    print("No beat...")
else:
    while counter < maximum - 1:
        second = second + beat + " "
        counter = counter + 1
        while counter == maximum:
            beat
            counter = counter + 1
print(second + beat)