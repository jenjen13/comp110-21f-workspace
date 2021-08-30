"""This program is computes less than, greater than or equal to, equal to, and not equal to."""
__author__ = "730404596"

left_side = int(input("Left-hand side: "))
right_side = int(input("Right-hand side: "))
ans_one = str(left_side < right_side)
ans_two = str(left_side >= right_side)
ans_three = str(left_side == right_side)
ans_four = str(left_side != right_side)
print(str(left_side) + " " + "<" + " " + str(right_side) + " " + "is" + " " + str(ans_one))
print(str(left_side) + " " + ">=" + " " + str(right_side) + " " + "is" + " " + str(ans_two))
print(str(left_side) + " " + "==" + " " + str(right_side) + " " + "is" + " " + str(ans_three))
print(str(left_side) + " " + "!=" + " " + str(right_side) + " " + "is" + " " + str(ans_four))