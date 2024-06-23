import math
max_num_lines = int(input("Please enter the number of lines: "))
count = 0 #track total number of lines printed
line_size = math.ceil(max_num_lines / 2) #create a var to track the mid point of the shape ie the longest part of the shape. Using math.ceil to make sure that the number is whole no matter the amount of lines
stars = "*" * line_size #declare stars to be printed

for i in range (0 ,max_num_lines):
    if count < line_size:
        count += 1 #increase count to keep track of number of lines printed
        print(stars[0:count]) #print a slice of stars based on what number is currently selected
    
    elif (count >= line_size & count <= max_num_lines):
        print(stars[0:(max_num_lines - count)]) #print stars less the number of lines that max_num_lines is greater than count
        count += 1 #increase count to keep track of number of printed lines but increases after the print as it will have been increased in the first if loop