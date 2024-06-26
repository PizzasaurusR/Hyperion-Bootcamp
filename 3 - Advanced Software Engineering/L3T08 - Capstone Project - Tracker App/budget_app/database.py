'''
The main program got very messy and difficult to read so I split the 
classes into separate files. This made it easier to read and modify
individual sections of the code.

This file is for the database operations.
'''
#-----------------------------------------------------------------------
# LIBRARY IMPORT
#-----------------------------------------------------------------------

import sqlite3
# Import classes from models.py
from models import Category, Transaction

#-----------------------------------------------------------------------
# CLASSES
#-----------------------------------------------------------------------
'''
This is the budget manager class.
The idea here is to be as modular as possible.
Method made to create tables.
'''
class BudgetManager:
    def __init__(self, db_name="budget.db"):
        self.conn = sqlite3.connect(db_name)
        # Call table creation method
        self.create_tables()


    def create_tables(self):
        '''
        Method to create the tables for transactions and for categories.
        When this method is called, both tables will be checked/created.
        Both methods follow this logic:

        1 - Create cursor
        2 - Check if table exists, if false create table.
        3 - All ids must be unique and will be set as the Primary Key
        4 - Commit changes

        transactions table uses a foreign key to connect to the 
        categories table.
        '''
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                          id INTEGER PRIMARY KEY,
                          name TEXT NOT NULL,
                          type TEXT NOT NULL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                          id INTEGER PRIMARY KEY,
                          amount REAL NOT NULL,
                          date TEXT NOT NULL,
                          category_id INTEGER,
                          description TEXT,
                          FOREIGN KEY(category_id) REFERENCE categories(id))
                       ''')
        # Commit changes
        self.conn.commit()

    
    def add_category(self, category):
        '''
        Method to add a category.
        '''
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO categories (name,type) VALUES (?, ?)", 
                       (category.name, category.type))
        # Commit changes
        self.conn.commit()

    
    def add_transaction(self, amount, date, category_id, description=""):
        '''
        Method to add transactions to database.
        '''
        self.cursor.execute('''INSERT INTO transactions (
                               amount, date, category_id, description) 
                               VALUES (?, ?, ?, ?)''', 
                               (amount, date, category_id, description))
        # Commit changes
        self.conn.commit()

    def close(self):
        '''
        Method to handle closing of database connections
        '''
        self.conn.close()
#-----------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------