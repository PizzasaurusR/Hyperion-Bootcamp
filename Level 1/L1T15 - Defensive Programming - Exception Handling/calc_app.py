#----------------------------------------------------------------------
'''
Calculator App

The way it works:
1 - Program starts up
2 - get_valid_function gets user input and checks to see if its an 
equation or one of the allowed operators.
3 - If it is an equation get_valid_input creates a list and calls on 
element_checks
4 - element_checks will check the validity of the equation.
5 - Valid equation is then pushed through the calculator app and the
the answer is stored as a result.
6 - The result is then appended onto the answers list and saved to file.
7- This is also displayed on screen.
7 - If get_valid_function returns "v" then the view_equation function is 
called to print to screen equation history 
8 - If get_valid_function returns "e" then the save_to_text_file 
function is called to add all answers to the file with new lines before
exit. 
9 - Any failed checks will result in an error message and redirection 
to the input screen.
'''
#----------------------------------------------------------------------


#----------------------------------------------------------------------
# FUNCTIONS
#----------------------------------------------------------------------

def calc_app(user_function):
    '''
    calc_func uses lists to dynamically check the function and apply the 
    correct calculation. 
    It will turn user input into a temp list reading the value in the 
    second position will determine the function applied. 
    Also checks for division by 0. 
    This seemed like the easiest place to put this check. 
    There is no other reason its here. 
    No need to create list here. It all comes in as a list already.
    '''

    # Assuming that function has made it past the checks and is a list
    # ans_list created to store all answers.
    temp_func_list = user_function
    ans_list = ""

    # Calculator function, checks operator and performs calculation 
    # based on operator. All equations that make it past the check will
    # be stored in ans_list
    if temp_func_list[1] == "*":
        result = multiply_numbers(int(temp_func_list[0]),
                                  int(temp_func_list[2])) 

    elif temp_func_list[1] == "+":
        result = add_numbers(int(temp_func_list[0]), int(temp_func_list[2]))   

    elif temp_func_list[1] == "-":
        result = minus_numbers(int(temp_func_list[0]), int(temp_func_list[2]))
       
    elif temp_func_list[1] == "/":
        result = divide_numbers(int(temp_func_list[0]), int(temp_func_list[2]))
        
    # Check if the result is an error message
    if isinstance(result, str):  
        return result
    ans_list = " ".join(temp_func_list) + f" = {result}"      
    return ans_list

def divide_numbers(num_1, num_2):
    '''
    This function handles division and checks for division by zero.
    '''
    if num_2 == 0:
        return "You are trying to divide by zero! Try again"
    return num_1 / num_2

def multiply_numbers(num_1, num_2):
    '''
    This function handles multiplication
    '''
    
    return num_1 * num_2

def add_numbers(num_1, num_2):
    '''
    This function handles addition
    '''

    return num_1 + num_2

def minus_numbers(num_1, num_2):
    '''
    This function handles subtraction
    '''

    return num_1 - num_2

def element_checks(user_function,allowed_operators):
    '''
    element_checks performs the following checks:

    1 - Checks to ensure that there are exactly 3 list items. This 
    ensures that there are not too many or too few items.
    2 - Checks that first element is an int.
    3 - Checks that third element is an int.
    4 - Checks to see if there is a valid operator ie + - * / 

    This is assuming that the function made it passed the first check 
    and is coming in as a list already
    '''

    check_list = user_function

    # Check the length of the list
    if len(check_list) != 3:
        print(("Whoops! Looks like you didn't enter enough values. " 
              "Remember you need an integer, then a space, " 
              "then an operator, then another space, "
              "then another integer."))
        return False
    
    # Check if the first element is an int
    try:
        int(check_list[0])
    except ValueError:
        print((f"Oh no! {check_list[0]} needs to be an integer. "
              "Please check your spaces and try again."))
        return False
    
    # Check if third element is an int
    try:
        int(check_list[2])
    except ValueError:
        print((f"Oh no! {check_list[2]} needs to be an integer. "
              "Please check your spaces and try again."))
        return False

    # Check if second element is in allowed_operators
    if check_list[1] not in allowed_operators:
        print(("Looks like you chose the wrong operators! Remember the "
              "operator has to be\n+ , - , * or /"))
        return False
    
    # If all checks pass return true
    return True

def get_valid_function(allowed_chars):
    '''
    get_valid_function:
    1 - Take user input
    2 - Create list
    3 - Checks if it is a valid function
    4 - If not valid asks for a new input
    6 - Checks for 'v' to view equation history
    7 - Checks for 'e' to exit the program

    This is the first check. I thought it was pretty cool that I could 
    build a check into the input and then loop it. Crazy

    So I decided to only save the valid equations and not error 
    messages. I also saved all of them. I can't imagine this use 
    creating a massive file. For more practical use I would add a date 
    to the file name. 

    Added extra line break for clarity when using the program for longer
    periods of time.
    '''

    while True:
        user_function = input("\nEnter a function with 2 integers and 1"
                              " operator.\nMake sure to add spaces"
                              " in between each number and operator.\n" 
                              "eg. 1 + 1\n"
                              "Push V to view all previous equations\n"
                              "Push E to exit\n")
        
        if len(user_function) == 1 and user_function.lower() == "v":
            return user_function.lower()
        
        elif len(user_function) == 1 and user_function.lower() == "e":
            return user_function.lower()
        
        valid_function_list = user_function.split()

        if element_checks(valid_function_list, allowed_chars):
            return valid_function_list
     
def save_to_txt_file(answer, filename="equations.txt"):
    '''
    save_to_txt_file prints all historic equations to a file called 
    equations.txt
    This was done last.
    ''' 

    try:
        with open(filename, 'a', encoding='utf-8') as file:
                file.write(answer + "\n")
    
    except IOError as error:
        print((f"Oof. There was an error trying to write to file: {error}"))

def view_equations(answers):
    '''
    View the previous answers that were provided
    '''

    if answers:
        print("Here are you previous equations:")
        for answer in answers:
            print(answer)
    else:
        print("No previous equations to display.")

#----------------------------------------------------------------------
# MAIN PROGRAM
#----------------------------------------------------------------------

'''
The idea was to have everything done using specialized functions that
 would act as multiple layers of protection.
Allowed operators was left outside for easier access in the need to make
 a change.
Answers list had to be stored here as it needed to last outside of the 
functions.
Auto save to file feature added. Viewing will still be possible but all
answers are saved to file automatically. Because of this I had to rework
the approach. 
'''

allowed_operators = ["+", "-", "/", "*"]
answers = []

while True:
    valid_function = get_valid_function(allowed_operators)

    if valid_function == 'v':
        view_equations(answers)

    elif valid_function == 'e':
        save_to_txt_file("\n".join(answers))
        print(("All previous equations have been printed to " 
              "'equations.txt' Exiting program"))
        break

    else:
        result = calc_app(valid_function)
        if result:
            print(result)
            answers.append(result)
            save_to_txt_file(result)
