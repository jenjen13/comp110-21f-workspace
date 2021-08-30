"""This program computes exponents, division, integer division, and remainder modulo."""
__author__ = "730404596"

left_side: int = int(input("Left-hand side: "))
right_side: int = int(input("Right-hand side: "))
ans_one = int(left_side ** right_side)
ans_two = float(left_side / right_side)
ans_three = int(left_side // right_side)
ans_four = int(left_side % right_side)
print(str(left_side) + " " + "**" + " " + str(right_side) + " " + "is" + " " + str(ans_one))
print(str(left_side) + " " + "/" + " " + str(right_side) + " " + "is" + " " + str(ans_two))
print(str(left_side) + " " + "//" + " " + str(right_side) + " " + "is" + " " + str(ans_three))
print(str(left_side) + " " + "%" + " " + str(right_side) + " " + "is" + " " + str(ans_four))