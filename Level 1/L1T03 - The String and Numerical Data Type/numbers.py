"""
get input number from user
assign to var first_num
get input number from user
assign to var sec_num
get input number form user
assign to var third_num

assign sum_var to the sum of all numbers
print out sum_var
subtract sec_num from first_num and assign to first_calc
print out first_calc
multiply third_num by first_num and assign to sec_calc
print out sec_calc
divide sum_var by third_num and assign to third_calc
print out third_calc
"""

first_num = int(input("Please enter the first number: "))
sec_num = int(input("Please enter the second number: "))
third_num = int(input("Please enter the third number: "))

sum_var = first_num + sec_num + third_num
print(sum_var)

first_calc = first_num - sec_num
print(first_calc)

sec_calc = third_num * first_num
print(sec_calc)

third_calc = sum_var / third_num
print(third_calc)

