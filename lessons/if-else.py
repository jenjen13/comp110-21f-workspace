"""Challenge Question #1"""

choice: int = int(input("enter a number: "))

# print A if choice < 25
# print B if choice >= 25 and < 50
# print c if choice > 75
# print d of choice >= 50 and <= 75

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("C")
        else:
            print("D")