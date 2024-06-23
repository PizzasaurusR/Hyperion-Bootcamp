"""
Compulsory Task 1: 
------------------

Copy the code provided below to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office 
   location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and 
   assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints 
   what the course is about and the name of the trainer by using the 
   description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints 
   the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the 
   following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the 
   terminal

Note: this task covers single inheritance. Multiple inheritance is also
possible in Python and we encourage you to do some research on 
multiple inheritance when you have finished this course.
"""
#----------------------------------------------------------------------
# CLASSES
#----------------------------------------------------------------------

class Course:

    # Set constant variables
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    # Init the lass and assign vars
    def __init__(self, name, contact_website):
        self.name = name
        self.contact_website = contact_website
        self.head_office_location = "Cape Town"  # Set head office

    def contact_details(self):
        print("\nPlease contact us by visiting", self.contact_website)

    def head_office_location(self):
        print(f"The head office location is {self.head_office_location}")

class OOPCourse(Course):
    '''
    Subclass of Course
    Must init description and trainer. These values are set.

    I set the values in the init call as they are permanent. Thanks to 
    YouTube, StackOverflow and www.w3schools.com for inspiration and
    help with implementation here.

    I used a super() to call the parent class constructor. Below is the
    research that I did and why I am using this particular call.

    Superclass: In object-oriented programming (OOP), a superclass 
    (or parent class) is the class from which other classes 
    (called subclasses or child classes) inherit attributes and methods.
    The superclass provides a blueprint or template that the subclasses 
    can extend or specialize.

    Usage: When a subclass inherits from a superclass, it gains access 
    to all public and protected attributes and methods of the 
    superclass. 
    This allows the subclass to reuse code from the superclass and build 
    upon it.

    I learnt that it is possible to init the name and contact_website
    again here eg:
    super().__init__(name="Fundamentals of Computer Science", 
                    contact_website="www.hyperiondev.com")
    I am not sure if it better practice to do this but it seemed like
    an unnecessary step so I did not add it as the values have already 
    been set in Course.
    '''
    def __init__(self, description="OOP Fundamentals", 
                 trainer="Mr Anon A. Mouse"):
        
        # Call and init superclass constructor
        super().__init__(self.name, self.contact_website)  
        
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        '''
        Function to display:
        1 - Name and description of course
        2 - The trainer for the course
        '''
        print(f"The course you are on is {self.name} and is about "
              f"{self.description}")
        print(f"Your trainer for this course is {self.trainer}")
        
    def show_course_id(self):
        print("Your course ID is: #12345") 

#----------------------------------------------------------------------
# MAIN PROGRAM
#----------------------------------------------------------------------

# Create object from subclass called course_1
course_1 = OOPCourse()

# Call methods to display information
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
