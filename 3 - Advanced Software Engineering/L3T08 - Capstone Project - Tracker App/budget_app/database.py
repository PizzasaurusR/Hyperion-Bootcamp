'''
The main program got very messy and difficult to read so I split the 
classes into separate files. This made it easier to read and modify
individual sections of the code.

This file is for the database operations.
Exception handling has been added.
'''
#-----------------------------------------------------------------------
# LIBRARY IMPORT
#-----------------------------------------------------------------------

import sqlite3
# Import classes from models.py
from models import Category, Transaction, Expense

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
        try:
            self.conn = sqlite3.connect(db_name)
            # Call table creation method
            self.create_tables()
        except sqlite3.Error as error:
            print(f"Error connecting to database: {error}")

    #-------------------------------------------------------------------
    # METHODS
    #-------------------------------------------------------------------
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

        Added in additional table for Expenses. I decided to 
        differentiate transactions and expenses. Main reason for this is
        that I forgot that the menu said "expenses" and in my head it 
        made more sense that they be called transactions.

        Expenses now mean a fixed amount that will be added to your
        deductibles. This can be input once and then added to all
        budget calculations. E.g. Rent, Car Payments, Medical Aid.
        '''
        try:
            cursor = self.conn.cursor()
            # Create 'categories' table if not exist 
            cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            type TEXT NOT NULL)''')
            
            # Create 'transactions' table if not exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY,
                            amount REAL NOT NULL,
                            date TEXT NOT NULL,
                            category_id INTEGER,
                            description TEXT,
                            FOREIGN KEY(category_id) REFERENCE categories(id))
                            ''')
            
            # Create 'expenses' table if not exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                              id INTEGER PRIMARY KEY,
                              name TEXT NOT NULL,
                              amount REAL NOT NULL,
                              category_id INTEGER,
                              FOREIGN KEY(category_id) REFERENCES categories(id
                              ))''')
            
            # Commit changes
            self.conn.commit()

        except sqlite3.Error as error:
            print(f"Error creating tables: {error}")

    
    def add_category(self, category):
        '''
        Add new category into 'categories' table
        '''
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO categories (name,type) VALUES (?, ?)", 
                            (category.name, category.type))
            # Commit changes
            self.conn.commit()
        except sqlite3.Error as error:
            print(f"Error adding category: {error}")

    
    def add_transaction(self, transaction):
        '''
        Add transactions to 'transactions' table.
        '''
        try:
            cursor = self.conn.cursor()
            category_id = self.get_category_id(transaction.category.name, 
                                               transaction.category.type)
            
            if category_id is not None:
                cursor.execute('''INSERT INTO transactions (
                                amount, date, category_id, description) 
                                VALUES (?, ?, ?, ?)''', 
                                (transaction.amount, transaction.date, 
                                 category_id, transaction.description))
                # Commit changes
                self.conn.commit()
            
            else:
                print("Category not found.")
        
        except sqlite3.Error as error:
            print(f"Error adding transaction: {error}")


    def add_expense(self, expense):
        '''
        Add expenses to 'expenses' table.
        '''
        try:
            cursor = self.conn.cursor()
            category_id = self.get_category_id(expense.category.name, 
                                               expense.category.type)
            
            if category_id is not None:
                cursor.execute('''INSERT INTO expenses (
                               name, amount, category_id) 
                               VALUES (?, ?, ?)''', 
                               (expense.name, expense.amount, category_id))
                # Commit changes
                self.conn.commit()


    def get_category_id(self, name, type):
        '''
        Method to fetch category_id from 'categories' table based on 
        name and type. 
        '''
        try:
            cursor = self.conn.cursor()
            cursor.execute('''SELECT id FROM categories WHERE name = ? AND
                              type = ?''', (name, type))
            result = cursor.fetchone()

            if result:
                return result[0]
            
            else:
                print("Category not found.")
                return None
        
        except sqlite3.Error as error:
            print(f"Error fetching category id: {error}")
            return None


    def view_categories(self):
        '''
        Method to fetch and display all categories in categories table.
        '''
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM categories")
            categories = cursor.fetchall()

            for category in categories:
                print(f"ID: {category[0]}, Name: {category[1]}, "
                      f"Type: {category[2]}")
                
        except sqlite3.Error as error:
            print(f"Error viewing categories: {error}")


    def view_transactions(self):
        '''
        View all transactions stored in the 'transactions' table based
        on a date range. Default is one month from the day of request.
        '''


    def view_expenses(self):
        """
        View all expenses stored in the 'expenses' table.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM expenses")
            expenses = cursor.fetchall()

            for expense in expenses:
                print(f"ID: {expense[0]}, Name: {expense[1]}, "
                      f"Amount: {expense[2]}, Category ID: {expense[3]}")
        
        except sqlite3.Error as error:
            print(f"Error viewing expenses: {error}")


    def close(self):
        '''
        Method to handle closing of database connections
        '''
        try:
            self.conn.close()
        except sqlite3.Error as error:
            print(f"Error closing table: {error}")
