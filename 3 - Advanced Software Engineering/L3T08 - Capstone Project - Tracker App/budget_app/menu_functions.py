#-----------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------
from models import Category, Transaction, Expense
from database import BudgetManager

#-----------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------

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


def view_transactions_by_category(budget_manager, user_id):
    print("Feature not implemented yet.")


def add_income(budget_manager, user_id):
    print("Feature not implemented yet.")


def view_income(budget_manager, user_id):
    print("Feature not implemented yet.")


def view_income_by_category(budget_manager, user_id):
    print("Feature not implemented yet.")


def set_budget_for_category(budget_manager):
    print("Feature not implemented yet.")


def view_budget_for_category(budget_manager):
    print("Feature not implemented yet.")


def set_financial_goals(budget_manager):
    print("Feature not implemented yet.")


def view_progress_towards_goals(budget_manager):
    print("Feature not implemented yet.")