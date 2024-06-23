# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the 
# error messages, and find and fix the errors.

animal = "Lion" #Syntax error - added ""
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal_type}. "
             f"It is a {animal} and it has {number_of_teeth} teeth") 
#Syntax error - added f for auto formatting. 
# Logic errors - changed animal to animal type. 
# Changed number_of_teeth to animal. 
# Changed animal_type to number_of_teeth

print(full_spec) #Syntax error - added ()
