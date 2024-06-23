#----------------------------------------------------------------------
'''
Recursion Sum App

This app is designed to take in a list of numbers from the user, get an 
index point from the user and then calculate the sum of the numbers up 
to the index point.

How it works:

class Email:
    
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

1 - Get the list of numbers
2 - Convert list into integers
3 - Get the length of the new integer list
4 - Get a valid index point
5 - If the index point is valid then call the recursion function
6 - Print out the list of numbers
7 - Print out the sum of the numbers up to the index
8 - Check if user would like to exit the app
'''
#----------------------------------------------------------------------
# FUNCTIONS
#----------------------------------------------------------------------
def get_numbers_list():
    '''
    This function gets user input for the number list.
    Input is taken in as string and then converted into a list/array
    I recently found out that strip and split can be done together so I 
    implemented a use case here.
    '''
    list_of_numbers = input("Please enter a list of numbers separated by " 
                            "spaces:\n"
                            "Eg 1 2 3 6 7 5 10 8 4 9 11...\n")
    
    numbers_list = list_of_numbers.strip().split(" ")
    return numbers_list

def get_index_point(numbers_list_len):
    '''
    Function to get a valid index point for use in recursion sum
    Takes user input and then checks to see if the number is valid.
    For index point to be valid it must be greater than -1 and smaller
    than the length of the numbers list.

    I used a while true loop to make sure that the user is returned back 
    to the input if an incorrect answer is given.

    Try-excepts are used to throw back an error message for an invalid 
    input
    '''
    # Get user input for index_point
    while True:
        index_point = input(f"Please enter a number between 0 "
                            f"and {numbers_list_len - 1}: ")
        
    # Convert input to int. If it can't be converted it's not a valid 
    # input

        try:
            index_point = int(index_point)
        except ValueError:
            print("That's not a valid input. Please input a number eg 4")
            continue

        #Check if index_point is actually in the list.    
        if 0 <= index_point < numbers_list_len:
            return index_point
        else: 
            print("That's not a valid index point. Try again")

def get_int_numbers_list(numbers_list):
    '''
    Quick function to change the numbers list into a list of integers
    This makes the calculations later on easier and checks to make sure
    that the numbers list has valid number inputs.

    If the check fails then the user is prompted to enter a number list 
    again.
    '''
    while True:
        try:
            int_numbers_list = [int(num) for num in numbers_list]
            return int_numbers_list
        except ValueError:
            print("Invalid input detected in numbers list. Remember to input "
                "digits only eg: 1 2 3")
            numbers_list = input("Please enter a list of numbers separated by " 
                            "spaces:\n"
                            "Eg 1 2 3 6 7 5 10 8 4 9 11...\n")

def sum_recursion(int_numbers_list, index_point):
    '''
    Recursive function to get the sum of the numbers in the number list 
    up to the index point. 

    So the way this works is that we check to see if the index point is 
    0. If it is then we return just the first value of the 
    int_numbers_list.

    If it is not then we grab the number in the current index position 
    and then add the number in the index position 1 below it ie 
    (index_point - 1). This is done by calling the sum_recursion func
    again.

    Now we check if the index_point is 0 again. If it is then we break
    out of the loop. If index_point is still greater than 0 we run the 
    loop again.

    This process will continue until the index point reaches 0 
    '''

    if index_point == 0:
        return int_numbers_list[0]
    else:
        return (int_numbers_list[index_point] + 
                sum_recursion(int_numbers_list, index_point - 1))

def main():
    '''
    This function runs the main program by automatically calling the 
    other functions.

    1 - Get the list of numbers
    2 - Convert list into integers
    3 - Get the length of the new integer list
    4 - Get a valid index point
    5 - If the index point is valid then call the recursion function
    6 - Print out the list of numbers
    7 - Print out the sum of the numbers up to the index
    8 - Check if user would like to exit the app

    Used a while loop to make sure that the user is prompted towards a 
    correct input.
    Added exit option as this was running in a permanent loop because of
    while loop. I wanted it to run this way so adding an exit was the 
    only way I could figure out how 
    '''
    while True:

        # Get the list of numbers.
        numbers_list = get_numbers_list()
    
        # Convert numbers_list to integers.
        # If get_int_numbers_list returns None(Invalid input), this 
        # function will attempt to get a valid input again. 
        int_numbers_list = get_int_numbers_list(numbers_list)
        if int_numbers_list is None:  
            continue  # Get user to input again on invalid input
    
        # Get length of the numbers list.
        numbers_list_len = len(int_numbers_list)
    
        # Get valid index_point from user.
        index_point = get_index_point(numbers_list_len)
    
        # Calculate sum using recursion up to the index point, if the 
        # get_index_point returns a valid number. 
        if index_point is not None:
            result = sum_recursion(int_numbers_list, index_point)
            print(int_numbers_list)
            print(f"The sum up to index {index_point} is: {result}")

        # Added exit option as the loop was running infinitely. 
        # Used .lower() to ensure no errors when accepting capitals.
        # This was done quick and dirty so any option other than Y/y 
        # will keep the program running.
        exit_app = input("Would you like to Exit? Y/N:\n").lower()
        if exit_app == 'y':
            break
        else:
            main()

#----------------------------------------------------------------------
# MAIN PROGRAM
#----------------------------------------------------------------------
'''
1 - Get the list of numbers
2 - Convert list into integers
3 - Get the length of the new integer list
4 - Get a valid index point
5 - If the index point is valid then call the recursion function
6 - Print out the list of numbers
7 - Print out the sum of the numbers up to the index
8 - Check if user would like to exit the app

Steps 1 - 8 run automatically on app start. 
I tried to make this as modular as possible to prep for OOP.
It's also just really cool to only have 1 line in my program that isn't
a function.
'''
# Execute the main function
main()
