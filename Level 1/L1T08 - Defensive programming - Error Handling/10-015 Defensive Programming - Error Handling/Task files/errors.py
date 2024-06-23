# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the 
# error messages, and find and fix the errors.

print("Welcome to the error program")  # Syntax error corrected, 
                                       #() added
print("\n") # Syntax error corrected, () added and indent removed

# Variables declaring the user's age, casting the str to an int, 
# and printing the result
age_Str = "24 years old"  # Syntax error corrected, indentation removed, 
                        # "==" changed to "=" for variable assignment. 
age = int(age_Str[0:2])  # Syntax error corrected, indentation removed. 
                        # logic error corrected - changed the allocation 
                        # of var age to the first 2 chars of age_Str, 
                        # removed int type allocation
print(f"I'm  {age}  years old.")  # Syntax error corrected - indentation 
                                # removed, spaces added for clarity.  
                                # Runtime error - Added auto formatting 
                                # to age

# Variables declaring additional years and printing the total years of 
# age
years_from_now = 3  # Syntax error corrected, indentation removed. 
                    # Logic error - changed var to int
total_years = age + years_from_now  #Syntax error corrected, indentation
                                    #removed

print(f"The total number of years: {total_years}")  #Syntax error 
                                                # corrected, indentation 
                                                # removed, () added to 
                                                # print. 
                                                # Runtime 
                                                # error - removed 
                                                # concat and added 
                                                # autoformatting,
                                                # changed 
                                                # answer_years to 
                                                # total_years.

# Variable to calculate the total amount of months from the total amount
# of years and printing the result
total_months = (total_years * 12) + 6  #Syntax error corrected, 
                                    # indentation removed. 
                                    # Logic error - Changed total to 
                                    # total_years. 
                                    # Added an additional 6 months in 
                                    # order to match prompt below.
print(f"In 3 years and 6 months, I'll be {total_months} months old") 
# Syntax error corrected, indentation removed, () added to print. 
# Logic error - instead of concatting total months 
# Runtime error - Added auto formatting

#HINT, 330 months is the correct answer
