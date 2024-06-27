#-----------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------

from models import User

#-----------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------

def login(budget_manager):
        '''
        Login function. Calls authentication methods to access user 
        profile.
        '''
        while True:
            print("--- Login Menu ---")
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = budget_manager.authenticate_user(username, password)
            
            if user_id:
                return user_id
            
            else:
                print("Invalid username or password. Please try again.")


def register(budget_manager):
        '''
        Function to register a new user profile.
        '''
        while True:
            print("--- Register Menu ---")
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            
            user = User(username, password)
            budget_manager.add_user(user)
            
            print("Registration successful. Please login.")
            return