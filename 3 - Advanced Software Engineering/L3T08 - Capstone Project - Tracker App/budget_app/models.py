'''
The main program got very messy and difficult to read so I split the 
classes into separate files. This made it easier to read and modify
individual sections of the code.

This file is for the category and transaction classes.
'''
class Category:
    '''
    Class to define Categories.
    __str__ was used to ensure that a string is returned when calling 
    the method.
    '''
    def __init__(self, name, type):
        self.name = name
        self.type - type

    def __str__(self):
        return f"Category: {self.name}, Type: {self.type}"
    

class Transaction:
    '''
    Class to define Transactions.
    __str__ was used to ensure that a string is returned when calling 
    the method.
    '''
    def __init__(self, amount, date, category, description=""):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def __str__(self):
        return (f"{self.category.type.capitalize()} - "
                f"{self.category.name}: {self.amount} on {self.date} -"
                f" {self.description}")

class Expense:
    '''
    Class to define Expenses.
    __str__ was used to ensure that a string is returned when calling 
    the method.
    '''
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def __str__(self):
        return (f"{self.category.type.capitalize()} - "
                f"{self.category.name}: {self.amount} on {self.date} -"
                f" {self.description}")
    
class User:
    '''
    Class to define Users.
    __str__ was used to ensure that a string is returned when calling 
    the method.
    '''
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"User: {self.username}"

    