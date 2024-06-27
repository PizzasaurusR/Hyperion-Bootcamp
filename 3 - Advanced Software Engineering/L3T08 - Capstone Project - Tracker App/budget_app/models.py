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
        self.type = type

    def __str__(self):
        return f"Category: {self.name}, Type: {self.type}"
    

class Transaction:
    '''
    Class to define Transactions.
    '''
    def __init__(self, amount, date, category, description=""):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description


class Expense:
    '''
    Class to define Expenses.
    '''
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    
class User:
    '''
    Class to define Users.
    '''
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Income:
    '''
    Class to define Income.
    '''
    def __init__(self, user_id, amount, date, category_id, description):
        self.user_id = user_id
        self.amount = amount
        self.date = date
        self.category_id = category_id
        self.description = description


class Goal:
    def __init__(self, user_id, description, target_amount, due_date):
        self.user_id = user_id
        self.description = description
        self.target_amount = target_amount
        self.due_date = due_date


class Saving:
    def __init__(self, user_id, amount, date_saved, goal_id=None):
        self.user_id = user_id
        self.amount = amount
        self.date_saved = date_saved
        self.goal_id = goal_id