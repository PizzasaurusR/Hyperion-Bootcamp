### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:
    '''
    Declare the class variable, with default value, for emails. 
 
    Initialise the instance variables for emails.

    Create the method to change 'has_been_read' emails from False to True.
    '''
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True
        

# --- Lists --- #
# Initialise an empty list to store the email objects.
Inbox = []

# --- Functions --- #

def populate_inbox():
   '''
   Create 3 sample emails and add it to the Inbox list.

   In this example I have used pre-filled email values.
   In an actual program I would iterate through the list of emails
   and pull in all the information using a for loop.
   ''' 
   email1 = Email("example1@gmail.com", 
                  "Welcome to HyperionDev!", 
                  "Content of the first email")
   email2 = Email("example2@gmail.com", 
                  "Great work on the bootcamp!", 
                  "Content of the second email")
   email3 = Email("example3@gmail.com", 
                  "Your excellent marks!", 
                  "Content of the third email")

   Inbox.append(email1)
   Inbox.append(email2)
   Inbox.append(email3)
     
def list_emails():
    '''
    Create a function which prints the email’s 
    subject_line, along with a corresponding number.

    Used enumerate to run through Inbox list to print all emails.
    '''
    
    for index, email in enumerate(Inbox):
        print(f"{index} - {email.subject_line}")

def read_email():
    '''
    Create a function which displays a selected email. 
    Once displayed, call the class method to set its 
    'has_been_read' variable to True.

    Use list_emails to create a list of all emails.

    If the index is valid then print the email information and mark as 
    read.

    Added ValueError to make sure that a valid option is selected.
    '''
    list_emails()

    try:
        index = int(input("\nEnter the index of the email you want to read: "))

        if 0 <= index < len(Inbox):
            email = Inbox[index]
            print(f"\nEmail Address: {email.email_address}")
            print(f"Subject Line: {email.subject_line}")
            print(f"Email Content: {email.email_content}\n")
            email.mark_as_read()
            print(f"Email from {email.email_address} marked as read.\n")
        
        else:
            print("Invalid index. Please try again.\n")

    except ValueError:
        print("Invalid input. Please enter a valid index number.\n")

def list_unread_emails():
    '''
    Create a list of all unread emails and then present a list of 
    options for the user to chose from.

    Create list containing index and email for Inbox list
    If the email has not been marked as read then add to unread_emails.
    Run through unread_emails and print index and email.

    If all emails are read then print message to tell user.
    '''
    print("\nUnread Emails:")
    unread_emails = [(index, email) for index, email in enumerate(Inbox) 
                     if not email.has_been_read]
    
    if unread_emails:
        for index, email in unread_emails:
            print(f"{index} - {email.subject_line}")

    else:
        print("No unread emails.")

    print()

def menu():
    '''
    Created function to control menu and menu options
    '''
    while True:
        print("\nEmail Menu")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application\n")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            read_email()
        elif choice == "2":
            list_unread_emails()
        elif choice == "3":
            print("Quitting application.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Call menu function to run the rest of the program
menu()
