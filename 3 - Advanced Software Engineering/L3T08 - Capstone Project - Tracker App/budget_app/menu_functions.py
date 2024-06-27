#-----------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------
import datetime
from models import Category, Transaction, Expense, Income
from database import BudgetManager

#-----------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------

# Add or update operators

def add_transaction(budget_manager, user_id):
    '''
    Function to collect user input to add a transaction
    '''
    try:
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        category_name = input("Enter category name: ")
        category_type = input("Enter category type (expense/income): ")
        description = input("Enter description: ")
        category = Category(category_name, category_type)
        transaction = Transaction(amount, date, category, description, user_id)

        if budget_manager.add_transaction(transaction):
            print("Transaction added successfully!")

        else:
            print("Failed to add transaction")
    
    except ValueError:
        print("Invalid input. Please ensure all entered values are correct.")
    
    except Exception as error:
        print(f"An error occurred: {error}")


def add_expense(budget_manager, user_id):
    '''
    Function to collect user input to add an expense.
    '''
    try:
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        category_name = input("Enter category name: ")
        category_type = input("Enter category type (expense/income): ")
        category = Category(category_name, category_type)
        expense = Expense(name, amount, category, user_id)
        
        if budget_manager.add_expense(expense):
            print("Expense added successfully.")
        
        else:
            print("Failed to add expense.")
    
    except ValueError:
        print("Invalid input. Please ensure all entered values are correct.")
    
    except Exception as error:
        print(f"An error occurred: {error}")


def add_income(budget_manager, user_id):
    '''
    Function to get user input and add income into 'incomes' table.
    '''
    try:
        amount = float(input("Enter the income amount: "))
        date = input("Enter the date of income (YYYY-MM-DD): ")
        category_id = int(input("Enter the category ID (or 0 if none): "))
        description = input("Enter a description for the income: ")
        
        # Assuming category_id of 0 means no specific category
        category_id = None if category_id == 0 else category_id
        
        income = Income(user_id, amount, date, category_id, description)
        
        if budget_manager.add_income(income):
            print("Income added successfully.")
        
        else:
            print("Failed to add income.")
    
    except ValueError:
        print("Invalid input. Please make sure all inputs are"
              " correctly formatted.")
    
    except Exception as error:
        print(f"An error occurred: {error}")


def set_financial_goals(budget_manager, user_id):
    '''
    Function to set financial goals in 'goals' table
    '''
    description = input("Enter the description of your financial goal: ")
    target_amount = float(input("Enter the target amount for your goal: "))
    due_date = input("Enter the due date for your goal (YYYY-MM-DD): ")
    success = budget_manager.add_goal(user_id, description, 
                                      target_amount, due_date)
    
    if success:
        print("Financial goal set successfully.")
    
    else:
        print("Failed to set financial goal.")


def set_budget_for_category(budget_manager, user_id):
    '''
    Function to get user input and set budget for categories.
    '''
    category_id = int(input("Enter the category ID for the budget: "))
    amount = float(input("Enter the budget amount: "))
    success = budget_manager.add_budget(category_id, user_id, amount)
    
    if success:
        print("Budget set successfully for the category.")
    
    else:
        print("Failed to set budget for the category.")


def add_saving(budget_manager, user_id):
    amount = get_valid_input("Enter the saving amount: ", float)
    
    date_saved = get_valid_input("Enter the date of saving (YYYY-MM-DD): ", 
                                 str, validate_date)
    
    goal_id = get_valid_input("Enter the goal ID to link this saving to "
                              "(or 0 if none): ", int)

    goal_id = None if goal_id == 0 else goal_id

    if budget_manager.add_saving(user_id, amount, date_saved, goal_id):
        print("Saving added successfully.")
    
    else:
        print("Failed to add saving.")

        
# Fetch operators

def view_transactions(budget_manager, user_id):
    '''
    Function to collect user input to view transactions
    '''
    try:
        start_date = input("Enter start date (YYYY-MM-DD) or leave blank: ")
        end_date = input("Enter end date (YYYY-MM-DD) or leave blank: ")
        transactions = budget_manager.view_transactions(user_id, 
                                                        start_date, end_date)
        if not transactions:
            print("No transactions found for the given date range.")
        
        else:
            for transaction in transactions:
                print(transaction)
    
    except Exception as error:
        print(f"An error occurred while retrieving transactions: {error}")


def view_transactions_by_category(budget_manager, user_id):
    '''
    Function to fetch and display all transactions by categories.
    '''
    category_name = input("Enter the category name to filter by: ")
    try:
        transactions = budget_manager.view_transactions_by_category(
            user_id, category_name)
        
        if not transactions:
            print("No transactions found for the specified category.")
        
        else:
            for transaction in transactions:
                print(f"ID: {transaction[0]}, "
                      f"Amount: {transaction[1]}, "
                      f"Date: {transaction[2]}, "
                      f"Description: {transaction[3]}, "
                      f"Category: {transaction[4]}")
    
    except Exception as error:
        print(f"An error occurred: {error}")


def view_expenses(budget_manager):
    '''
    Function to view expenses.
    '''
    try:
        expenses = budget_manager.view_expenses()
        
        if not expenses:
            print("No expenses found.")
        
        else:
            for expense in expenses:
                print(expense)
    
    except Exception as error:
        print(f"An error occurred while retrieving expenses: {error}")


def view_income(budget_manager, user_id):
    '''
    Function to view user income/s.
    '''
    incomes = budget_manager.view_income(user_id)
    
    if not incomes:
        
        print("No income records found.")
    
    else:
        for income in incomes:
            print(f"Income ID: {income[0]}, Amount: {income[2]}, "
                  f"Date: {income[3]}, Category ID: {income[4]}, "
                  f"Description: {income[5]}")


def view_income_by_category(budget_manager, user_id):
    '''
    Function to view user income/s by category
    '''
    category_id = int(input("Enter the category ID to filter by: "))
    incomes = budget_manager.view_income_by_category(user_id, category_id)
    
    if not incomes:
        print("No income records found for this category.")
    
    else:
        for income in incomes:
            print(f"Income ID: {income[0]}, Amount: {income[2]}, "
                  f"Date: {income[3]}, Category ID: {income[4]}, "
                  f"Description: {income[5]}")


def view_budget_for_category(budget_manager, user_id):
    '''
    Function to call get_budget_for_category and then display budget 
    amounts
    '''
    category_id = int(input("Enter the category ID to view the budget: "))
    budget = budget_manager.get_budget_for_category(category_id, user_id)
    
    if budget:
        print(f"Budget for Category ID {category_id}: "
              f"{budget['budget_amount']}")
    
    else:
        print("No budget set for this category.")


def view_progress_towards_goals(budget_manager, user_id):
    '''
    Function to display progress towards goals.
    '''
    goals = budget_manager.view_progress_towards_goals(user_id)
    
    if not goals:
        print("No financial goals or savings found.")
    
    else:
        for goal in goals:
            print(f"Goal: {goal['description']}, "
                  f"Target: {goal['target_amount']}, "
                  f"Due Date: {goal['due_date']}, "
                  f"Saved: {goal['total_saved']}")


# Get Valid input operators

def validate_date(date_text):
    '''
    Validates the date format YYYY-MM-DD.
    '''
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        
        return True
    
    except ValueError:
        return False

def get_valid_input(prompt, value_type=float, validator=None):
    '''
    Function to get validated user input.
    '''
    while True:
        user_input = input(prompt)
        
        try:
            user_input = value_type(user_input)
            
            if validator and not validator(user_input):
                raise ValueError("Validation failed.")
            
            return user_input
        
        except ValueError as error:
            print(f"Invalid input ({error}). Please try again.")

