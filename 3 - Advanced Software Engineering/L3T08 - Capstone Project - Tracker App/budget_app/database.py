'''
The main program got very messy and difficult to read so I split the 
classes into separate files. This made it easier to read and modify
individual sections of the code.

This file is for the database operations.
Exception handling has been added.

Added user table and modified all searches to be based on a user profile
'''
#-----------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------
import datetime
import sqlite3
# Import classes from models.py
from models import Category, Transaction, Expense, User
# Import error handle decorator
from error_handler import handle_db_errors

#-----------------------------------------------------------------------
# CLASSES
#-----------------------------------------------------------------------
'''
This is the budget manager class.
The idea here is to be as modular as possible.
Method made to create tables.
'''
class BudgetManager:
    def __init__(self, db_name: str = "budget.db"):
        try:
            self.conn = sqlite3.connect(db_name)
            # Call table creation method
            self.create_tables()

        except sqlite3.Error as error:
            print(f"Error connecting to database: {error}")
    
    #-------------------------------------------------------------------
    # METHODS
    #-------------------------------------------------------------------
    
    @handle_db_errors
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

        Added 'user' table.
        '''
        cursor = self.conn.cursor()
        # Create 'categories' table if not exist 
        cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      type TEXT NOT NULL)''')

        # Create 'users' table if not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY,
                      username TEXT NOT NULL UNIQUE,
                      password TEXT NOT NULL)''')

        # Create 'transactions' table if not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                      id INTEGER PRIMARY KEY,
                      user_id INTEGER,
                      amount REAL NOT NULL,
                      date TEXT NOT NULL,
                      category_id INTEGER,
                      description TEXT,
                      FOREIGN KEY(category_id) REFERENCES categories(id),
                      FOREIGN KEY(user_id) REFERENCES users(id))''')
            
        # Create 'expenses' table if not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                      id INTEGER PRIMARY KEY,
                      user_id INTEGER,
                      name TEXT NOT NULL,
                      amount REAL NOT NULL,
                      category_id INTEGER,
                      FOREIGN KEY(category_id) REFERENCES categories(id),
                      FOREIGN KEY(user_id) REFERENCES users(id))''')
        
        # Create 'income' table if not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS income (
                      id INTEGER PRIMARY KEY,
                      user_id INTEGER,
                      amount REAL NOT NULL,
                      date TEXT NOT NULL,
                      category_id INTEGER,
                      description TEXT,
                      FOREIGN KEY(category_id) REFERENCES categories(id),
                      FOREIGN KEY(user_id) REFERENCES users(id))''')
        
        # Create 'goals' table if not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS goals (
                      id INTEGER PRIMARY KEY,
                      user_id INTEGER,
                      goal_description TEXT,
                      target_amount REAL,
                      due_date TEXT,
                      FOREIGN KEY(user_id) REFERENCES users(id))''')
            
        # Create 'budget' table if not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
                      id INTEGER PRIMARY KEY,
                      category_id INTEGER,
                      user_id INTEGER,
                      budget_amount REAL,
                      FOREIGN KEY(category_id) REFERENCES categories(id),
                      FOREIGN KEY(user_id) REFERENCES users(id))''')
        
        # Create 'savings' table if not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS savings (
                      id INTEGER PRIMARY KEY,
                      user_id INTEGER,
                      amount REAL NOT NULL,
                      date_saved TEXT NOT NULL,
                      goal_id INTEGER, 
                      FOREIGN KEY(user_id) REFERENCES users(id),
                      FOREIGN KEY(goal_id) REFERENCES goals(id))''')
        
        # Commit changes
        self.conn.commit()
    
    # Add or update operators
    @handle_db_errors
    def add_category(self, category):
        '''
        Add new category into 'categories' table
        '''
        cursor = self.conn.cursor()

        try:
            cursor.execute("INSERT INTO categories (name,type) VALUES (?, ?)",  
                           (category.name, category.type))
            # Commit changes
            self.conn.commit()
            return True  # Indicate success
        
        except sqlite3.Error:
            return False  # Indicate failure

    
    @handle_db_errors
    def add_transaction(self, transaction, user_id):
        '''
        Add transactions to 'transactions' table.
        '''
        cursor = self.conn.cursor()
        category_id = self.get_category_id(transaction.category.name, 
                                            transaction.category.type)
            
        if category_id:
            try:
                cursor.execute('''INSERT INTO transactions (
                                user_id, amount, date, category_id, 
                               description) VALUES (?, ?, ?, ?, ?)''', 
                                (user_id, transaction.amount, 
                                 transaction.date, category_id, 
                                 transaction.description 
                                ))
                # Commit changes
                self.conn.commit()
                return True  # Successful addition
            
            except sqlite3.Error:
                return False  # Error occurred
        
        else:
            print("Category not found.")
            return False  # Category not found
        

    @handle_db_errors
    def add_expense(self, expense, user_id):
        '''
        Add expenses to 'expenses' table.
        '''
        cursor = self.conn.cursor()
        category_id = self.get_category_id(expense.category.name, 
                                               expense.category.type)
            
        if category_id:
            try:
                cursor.execute('''INSERT INTO expenses (
                                user_id, name, amount, category_id) 
                                VALUES (?, ?, ?)''', 
                                (user_id, expense.name, expense.amount, 
                                 category_id))
                # Commit changes
                self.conn.commit()
                return True  # Expense added
            
            except sqlite3.Error:
                return False  # Error in adding
            
        else:
            print("Category not found.")
            return False  # Category not found


    @handle_db_errors
    def add_user(self, user):
        '''
        Add username and password to 'users' table.
        '''
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO users (username, password) 
                        VALUES (?, ?)''', (user.username, user.password))
        # Commit changes
        self.conn.commit()
        

    @handle_db_errors
    def authenticate_user(self, username, password):
        '''
        Method to authenticate user on login
        '''
        cursor = self.conn.cursor()
        cursor.execute('''SELECT id FROM users WHERE 
                        username = ? AND password = ?''', 
                        (username, password))
        result = cursor.fetchone()
            
        if result:
            return result[0]
            
        else:
            return None


    @handle_db_errors
    def add_income(self, income, user_id):
        '''
        Method to add income into 'incomes' table
        '''
        cursor = self.conn.cursor()
        
        try:
            cursor.execute('''INSERT INTO income 
                           (user_id, amount, date, category_id, description) 
                           VALUES (?, ?, ?, ?, ?)''',
                        (income.user_id, income.amount, income.date, 
                         income.category_id, income.description))
            
            self.conn.commit()
            return True
        
        except sqlite3.Error as error:
            print(f"Failed to add income: {error}")
            return False


    @handle_db_errors
    def add_budget(self, category_id, user_id, budget_amount):
        '''
        Method to add budget into 'budgets' table
        '''
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO budgets 
                       (category_id, user_id, budget_amount) 
                       VALUES (?, ?, ?)''', 
                       (category_id, user_id, budget_amount))
        self.conn.commit()
        
        return True
    

    @handle_db_errors
    def add_goal(self, user_id, description, target_amount, due_date):
        '''
        Method to add financial goals in 'goals' table
        '''
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO goals 
                      (user_id, goal_description, target_amount, due_date) 
                      VALUES (?, ?, ?, ?)''', 
                      (user_id, description, target_amount, due_date))
        
        self.conn.commit()
        
        return True
    

    @handle_db_errors
    def add_saving(self, user_id, amount, date_saved, goal_id = None):
        '''
        Method to add savings in 'savings' table
        '''
        cursor = self.conn.cursor()
        
        try:
            cursor.execute('''INSERT INTO savings 
                           (user_id, amount, date_saved, goal_id) 
                           VALUES (?, ?, ?, ?)''', 
                           (user_id, amount, date_saved, goal_id))
            self.conn.commit()
            return True
        
        except sqlite3.Error:
            self.conn.rollback()
            return False

# Fetch Operators
    @handle_db_errors
    def get_category_id(self, name, type):
        '''
        Method to fetch category_id from 'categories' table based on 
        name and type. 
        '''
       
        cursor = self.conn.cursor()
        cursor.execute('''SELECT id FROM categories WHERE name = ? AND
                        type = ?''', (name, type))
        result = cursor.fetchone()

        if result:
            return result[0]
            
        else:
            print("Category not found.")
            return None
        

    @handle_db_errors
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


    @handle_db_errors
    def view_transactions(self, user_id, start_date=None, end_date=None):
        '''
        View all transactions stored in the 'transactions' table based
        on a date range. Default is one month from the day of request.

        I'm damn proud of this. Created a variable query based on if the
        user enters a date.
        '''
        cursor = self.conn.cursor()
        query = "SELECT * FROM transactions WHERE user_id = ?"
        params = [user_id]

        if start_date and end_date:
            query += " AND date BETWEEN ? AND ?"
            params.extend([start_date, end_date])

        cursor.execute(query, params)
        transactions = cursor.fetchall()

        return transactions # Return list of transactions. Empty if none


    @handle_db_errors
    def view_transactions_by_category(self, user_id, category_name):
        '''
        Method to fetch and display all transactions by categories.
        '''
        cursor = self.conn.cursor()
    
        try:
            cursor.execute('''
                SELECT t.id, t.amount, t.date, t.description, 
                        c.name as category_name
                FROM transactions t
                JOIN categories c ON t.category_id = c.id
                WHERE t.user_id = ? AND c.name = ?
            ''', (user_id, category_name))
        
            transactions = cursor.fetchall()
            # Returns a list of transactions in the given category
            return transactions  
    
        except sqlite3.Error as error:
            print(f"Database error: {error}")
            return []  # Return an empty list if an error occurs


    @handle_db_errors
    def view_expenses(self, user_id):
        '''
        View all expenses stored in the 'expenses' table.
        '''
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE user_id = ?", (user_id))
        expenses = cursor.fetchall()

        return expenses  # Return list of expenses. Empty if none.        


    @handle_db_errors
    def view_income(self, user_id):
        '''
        View all user income/s stored in the 'incomes' table.
        '''
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM income WHERE user_id = ?", (user_id))
        incomes = cursor.fetchall()
        
        return incomes


    @handle_db_errors
    def view_income_by_category(self, user_id, category_id):
        '''
        View all user income/s stored in the 'incomes' table based on 
        category.
        '''
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM income WHERE 
                       user_id = ? AND category_id = ?''', 
                       (user_id, category_id))
        incomes = cursor.fetchall()
        
        return incomes


    @handle_db_errors
    def get_budget_for_category(self, category_id, user_id):
        '''
        Get user budget for each category. For use when viewing budgets.
        '''
        cursor = self.conn.cursor()
        cursor.execute('''SELECT budget_amount FROM budgets WHERE 
                       category_id = ? AND user_id = ?''', 
                       (category_id, user_id))
        result = cursor.fetchone()
        
        return {'budget_amount': result[0]} if result else None


    @handle_db_errors
    def get_goals(self, user_id):  
        cursor = self.conn.cursor()
        cursor.execute('''SELECT goal_description, target_amount, due_date 
                       FROM goals WHERE user_id = ?''', (user_id))
        
        return [
            {'description': row[0], 'target_amount': row[1], 
             'due_date': row[2]} for row in cursor.fetchall()]


    @handle_db_errors
    def view_savings(self, user_id):
        '''
        View all user savings stored in the 'savings' table.
        '''
        cursor = self.conn.cursor()
        cursor.execute('''SELECT amount, date_saved, goal_id 
                       FROM savings WHERE user_id = ?''', (user_id))
        
        return [{'amount': row[0], 'date_saved': row[1], 'goal_id': row[2]}
                 for row in cursor.fetchall()]


    @handle_db_errors
    def view_progress_towards_goals(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT g.goal_description, g.target_amount, 
                        g.due_date, IFNULL(SUM(s.amount), 0) as total_saved
                        FROM goals g
                        LEFT JOIN savings s 
                        ON g.id = s.goal_id AND s.user_id = g.user_id
                        WHERE g.user_id = ?
                        GROUP BY g.id''', (user_id))
        goals = cursor.fetchall()
        
        for goal in goals:
            print(f"Goal: {goal[0]}, Target: {goal[1]}, "
                  f"Due Date: {goal[2]}, Saved: {goal[3]}")


    @handle_db_errors
    def close(self):
        '''
        Method to handle closing of database connections
        '''
        self.conn.close()
        
