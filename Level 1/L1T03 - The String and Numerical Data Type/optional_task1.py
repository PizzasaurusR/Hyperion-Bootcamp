"""
get user input for var side1
get user input for side2
get user input for side3

calculate new var s where s = (side1 + side2 + side3) / 2
calculate var tri_area using math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
print tri_area
"""
import math

side1 = int(input("Please enter the length of the first side of the triangle: "))
side2 = int(input("Please enter the length of the second side of the triangle: "))
side3 = int(input("Please enter the length of the third side of the triangle: "))

s = (side1 + side2 + side3) / 2

tri_area = math.sqrt((s * (s - side1) * (s - side2) * (s - side3)))
print(tri_area)