'''
1 - Get user input for max number of lines
2 - Create a var to track the midpoint of the shape. This is the longest
    line of the shape.
    Using math.ceil to ensure that the number is whole, no matter the 
    amount of lines.
3 - The line of stars (*) is created based on the midpoint length.
4 - Starting from 1 till the midpoint, increase count and print a slice
    of the line of stars based on the number that count currently is.
5 - From the midpoint on, print stars less the the difference of 
    max_num_lines and count.
6 - Increase count to keep track of number of printed lines but 
    increases after the print as it will have been increased in the 
    first if loop.
'''

import math

max_num_lines = int(input("Please enter the number of lines: "))

# Track total number of lines printed.
count = 0 

# Create a var to track the mid point of the shape. 
line_size = math.ceil(max_num_lines / 2) 

# Declare stars to be printed
stars = "*" * line_size 

for i in range (0 ,max_num_lines):
    if count < line_size:
        # Increase count to keep track of num lines printed
        count += 1 
        # Print a slice of stars based on what num is currently selected
        print(stars[0:count]) 
    
    elif (count >= line_size & count <= max_num_lines):
        # Print Stars
        print(stars[0:(max_num_lines - count)]) 
        count += 1 
        