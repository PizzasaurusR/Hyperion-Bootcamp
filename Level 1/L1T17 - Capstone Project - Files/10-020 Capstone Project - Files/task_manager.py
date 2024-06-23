#----------------------------------------------------------------------
'''
Task Manager App

How it works:
1 - Takes user name and password from user
2 - Checks if user name is valid and password correct
3 - Checks if user is admin
4 - If admin then user gets admin menu
5 - If not then user gets standard menu
6 - admin can see stats and register new users
7 - All users can view all tasks, view current users tasks, add a task
and exit.
'''
#=====importing libraries===========
'''
Google helped me find some niche libraries to use to make the program
more robust.

getpass - For hiding password when registering new user
datetime - For getting the current days date when assigning tasks
sys - According to stack overflow this is a good way to make a clean 
exit. My understanding is that is allows us the option of exiting the 
program without any additional code being executed. It also helps with
exception handling.

'''
import getpass 
import datetime
import sys 
#----------------------------------------------------------------------
# FUNCTIONS
#----------------------------------------------------------------------
def get_user_credentials():
    '''
    Function to fetch user credentials from user.txt and return as a 
    dictionary.
    This function used to be 2 separate ones but after some work
    I was able to get to this. YouTube and stackOverflow were a major 
    help.
    Added file not found exception
    '''
    correct_user_credentials = {}
    try:
        with open('user.txt', 'r', encoding='utf-8') as user_file:
            for line in user_file:
                user_name, password = line.strip().split(',')
                correct_user_credentials[user_name] = password.strip()
    except FileNotFoundError:
        print("Error: 'user.txt' not found.")
    except Exception as error:
        print(f"An error occurred: {error}")
    return correct_user_credentials

def get_login():
    '''
    1 - Get the users login information.
    2 - First get username
    3 - Check user is valid. If true go to 4, If false go to 9 
    4 - Get Password.
    5 - Check password is valid. If true go to 6, If false go to 10
    6 - Login successful
    7 - Call main_menu
    8 - Exit get_login
    9 - Prompt user for new username input
    10 - Prompt user for new password

    Added getpass here for consistency in the program
    Now returns user_name for use in admin menu and view_my_tasks
    '''
    correct_user_credentials = get_user_credentials()

    while True:
        user_name = input("Enter Username: ")

        if user_name in correct_user_credentials:
            user_password = getpass.getpass("Enter Password: ")

            if user_password == correct_user_credentials[user_name]:
                print("\nLogin successful!\n")
                return user_name  # Return the logged-in user name
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username not found. Please try again")

def register_user():
    '''
    Function to register a new user

    1 - Takes new_user
    2 - Take in new_password
    3 - Take in confirm_password
    4 - If new_password and confirm_password are the same then ask for
    confirmation of registration
    5 - If Y then append user.txt
    6 - If N then cancel and move to step 1
    7 - If Passwords don't match ask for new password

    Added getpass after the fact. I just thought it would be a nice 
    feature to have and a libraries section was added.
    '''
    while True:
        new_user = input("Please enter the new username: ")
        new_password = getpass.getpass("Please enter the new password: ")
        confirm_password = getpass.getpass("Please confirm the password: ")

        if new_password == confirm_password:
            confirmation = input(f'''You are about to register:
New User: {new_user}
New Password: {new_password}

Please confirm (Y/N)
: ''').lower()
            
            if confirmation == 'y':
                with open('user.txt', 'a', encoding='utf-8') as user_file:
                    user_file.write(f"\n{new_user}, {new_password}")
                print("New user registered successfully!\n")
                return  # Exit the function on successful registration
            else:
                print("Registration cancelled. Please start over.")
        else:
            print("Passwords do not match. Please try again.")

def format_date(date_str):
    '''
    Ok so I realized that there are many ways to enter the date. So to 
    compensate for this I created a datetime object to convert the date
    str into the specified format(%d-%m-%Y)
    
    Then I converted the object into a str with the format(%d %b %Y).
    This is all done in a try-except block so that if there is an error
    then we can throw an exception.

    After testing the format date now runs several checks for most major
    date formats. Each time an exception is thrown it will then try a
    different format.

    All accepted formats are still returned as 10 Oct 2019

    '''
    try:
        date_obj = datetime.datetime.strptime(date_str, '%d-%m-%Y')
        return date_obj.strftime('%d %b %Y') 
    
    except ValueError:
        try:
            date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')
            return date_obj.strftime('%d %b %Y')  
        
        except ValueError:
            try:
                date_obj = datetime.datetime.strptime(date_str, '%d %b %Y')
                return date_obj.strftime('%d %b %Y')  
            
            except ValueError:
                print(f"Date '{date_str}' is not in the expected format. "
                      f"Please try again.")
                return None # If no format is found.
            
def get_new_task_details():
    '''
    1 - Get the assigned user
    2 - Get task title
    3 - Get task description
    4 - Set assigned date to current date
    5 - Get task due date
    6 - Set complete status to "No"

    Function to get new task details from the user
    Split off from add_tasks as it became cluttered.

    I used the datetime function here to set the assigned date.
    I'll be honest I don't really know how it works but it does.
    '''
    print("\nPlease enter New Task information:\n")
    new_task_user = input("Please enter the new task's allocated user: ")
    new_task_title = input("Please enter the new task's name: ")
    new_task_desc = input("Please enter the new task's description: ")
    new_task_assigned_date = datetime.datetime.today().strftime('%d-%m-%Y') 
    new_task_due_date = input("Please enter the new task's due date: ")
    new_task_complete_status = "No"

    return (
        new_task_user, 
        new_task_title, 
        new_task_desc, 
        new_task_assigned_date, 
        new_task_due_date, 
        new_task_complete_status
        )

def add_task():
    '''
    Function to add a new task
    1 - Get the task details using the get_new_task_details function
    2 - Display details and get confirmation
    3 - On confirmation append file
    4 - Else loop back to start of function

    Function now also loops through the due date to ensure that the 
    format is recognized. This is not necessary for the assigned date
    as the date is not inputted and can be controlled.
    '''
    while True:
        task_details = get_new_task_details()

        # Format the due date input
        due_date = format_date(task_details[4])

        if due_date:
            confirmation = input(f'''
You are about to add the following task:
Assigned User: {task_details[0]}
Task Title: {task_details[1]}
Task Description: {task_details[2]}
Assigned Date: {format_date(task_details[3])}
Due Date: {due_date}
Complete Status: {task_details[5]}

Please confirm (Y/N)\n: ''').lower()
            
            if confirmation == 'y':
                with open('tasks.txt', 'a', encoding='utf-8') as task_file:
                    task_file.write(f"\n{task_details[0]}, {task_details[1]}, "
                                    f"{task_details[2]}, "
                                    f"{format_date(task_details[3])}, "
                                    f"{due_date}, {task_details[5]}")
                print("New task added successfully!\n")
                return 
            
            else:
                print("Task allocation cancelled. Please start again.\n")

        else:
            print("Invalid date format. Please try again.")

def view_all_tasks():
    '''
    We open the .txt file and we assign each line as an element in 
    all_tasks.
    We then check if all_tasks is empty
    Then we run a for loop to take each element of all_tasks and we 
    split it into a new list. 
    Each element of the list is the assigned to a new var.
    Print out the details and start at the beginning of the for loop.
    '''
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as task_file:
            all_tasks = task_file.readlines()

        if not all_tasks:
            print("No tasks found.")
            return

        print("\nAll Tasks:\n")
        for task in all_tasks:
            task_details = [item.strip() for item in task.split(',')]
            # Unpack task details
            assigned_user, task_title, task_desc, assigned_date, due_date, complete_status = task_details
            
            print(f'''
Assigned User: {assigned_user}
Task Title: {task_title}
Task Description: {task_desc}
Assigned Date: {assigned_date}
Due Date: {due_date}
Complete Status: {complete_status}
\n=====================================''')

    except FileNotFoundError:
        print("Tasks file not found.")

    except Exception as error:
        print(f"An error occurred: {error}")

def view_my_tasks(current_user):
    '''
    Function to view tasks assigned to the current user.

    Copied view_all_tasks and changed it to be used for just the current
    user.

    We open the .txt file and we assign each line as an element in 
    all_tasks.
    We then check if all_tasks is empty
    Then we run a for loop to take each element of all_tasks and we 
    split it into a new list. 
    Each element of the list is the assigned to a new var.
    Check to see if assigned user is the current user.
    If yes, print out the details and start at the beginning of the 
    for loop.
    '''
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as task_file:
            all_tasks = task_file.readlines()

        if not all_tasks:
            print("No tasks found.")
            return

        print(f"\nTasks for {current_user}:")
        for task in all_tasks:
            task_details = [item.strip() for item in task.split(',')]
            # Unpack task details
            assigned_user, task_title, task_desc, assigned_date, due_date, complete_status = task_details
            
            if assigned_user == current_user:
                print(f'''
Assigned User: {assigned_user}
Task Title: {task_title}
Task Description: {task_desc}
Assigned Date: {assigned_date}
Due Date: {due_date}
Complete Status: {complete_status}
\n=====================================''')

    except FileNotFoundError:
        print("Tasks file not found.")

    except Exception as error:
        print(f"An error occurred: {error}")

def exit_program():
    '''
    Function to exit the program
    sys.exit used for a cleaner exit
    '''
    print("Exiting program.")
    sys.exit()

def get_stats():
    """
    This function counts the lines in tasks.txt and user.txt and then
    prints out the totals
    """
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as task_file:
            task_count = len(task_file.readlines())
        
        with open('user.txt', 'r', encoding='utf-8') as user_file:
            user_count = len(user_file.readlines())
        
        print(f"\nTotal number of tasks: {task_count}")
        print(f"Total number of users: {user_count}\n")
    
    except FileNotFoundError:
        print("Error: Required files ('tasks.txt' or 'user.txt') not found.")
    except Exception as error:
        print(f"An error occurred: {error}")
    
def main_menu():
    '''
    Function to display the main menu and handle user input

    Gets a user input and then calls a function based on what that 
    input is.

    Now stores current user for use in view_my_tasks and admin menu 
    access 
    '''
    current_user = get_login()

    while True:
        if current_user == "admin":
            menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - statistics
e - exit
: ''').lower()
            
        else:
            menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
        
        if menu == 'r'and current_user == 'admin':
            register_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_tasks()
        elif menu == 'vm':
            view_my_tasks(current_user)
        elif menu == 'e':
            exit_program()
            break
        elif menu == 's' and current_user == "admin":
            get_stats()
        else:
            print("Invalid option. Please try again.")

#----------------------------------------------------------------------
# Main Program
#----------------------------------------------------------------------

main_menu()
