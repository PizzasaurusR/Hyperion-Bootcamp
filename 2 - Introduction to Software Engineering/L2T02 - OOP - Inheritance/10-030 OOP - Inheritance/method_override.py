#----------------------------------------------------------------------
# CLASSES
#----------------------------------------------------------------------
class Adult:
    '''
    Init Adult class with name, age, eye_colour and, hair_colour.
    Run check on age to determine if the user can drive.
    I wanted to call the class directly in the if statement but couldn't
    get it to work. 
    Instead what I did was make sure that the Child class displays a 
    different message to the Adult class.
    '''
    # Init class and set attributes
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # Method to set can_drive based on age
    def can_drive(self):

        if self.age >= 18:
            print(f"{self.name} is old enough to drive.")
        else: #This is redundant. Addressed below in Child object
            print(f"{self.name} is not old enough to drive.")

class Child(Adult):
    '''
    Child class to superclass Adult.
    Inherits attributes from Adult class.
    Overrides can_drive in Adult class to display appropriate message.
    '''
    def can_drive(self):
        print(f"{self.name} is too young to drive.")
#----------------------------------------------------------------------
# FUNCTIONS
#----------------------------------------------------------------------
def create_person():
    '''
    Create a "Person" by getting inputs from user.
    Check user age.
    If age is less than 18 then set user as Child.
    If age is greater than or equal to 18 then set user as Adult.
    Calls the can_drive function after the object is made.

    I had to create a person before I could do the checks and assign
    the correct classes.

    Program originally assumed the correct value types of inputs.
    Added exception handling to make sure that the correct type of 
    values are inserted.
    '''
     
    while True:
        # Get user inputs for class attributes
        name = input("Enter name: ")
        try:
            age = int(input("Enter age: "))
            if age < 0:
                raise ValueError("Age must be a positive integer.")
            eye_colour = input("Enter eye colour: ")
            hair_colour = input("Enter hair colour: ")

            # Check types of inputs and makes sure they are valid
            if not isinstance(name, str):
                raise ValueError("Error: Name must be a string.")
            if not isinstance(age, int):
                raise ValueError("Error: Age must be an integer.")
            if not isinstance(eye_colour, str):
                raise ValueError("Error: Eye colour must be a string.")
            if not isinstance(hair_colour, str):
                raise ValueError("Error: Hair colour must be a string.")
            
            break  # Exit the loop if inputs are valid

        except ValueError as value_error:
           print(f"Invalid input: {value_error}. Please try again.")

   # Check age and decide if person is a child or an adult
    if age >= 18:
        person = Adult(name, age, eye_colour, hair_colour)
    else:
        person = Child(name, age, eye_colour, hair_colour)

    person.can_drive()

#----------------------------------------------------------------------
# MAIN PROGRAM
#----------------------------------------------------------------------

create_person()
