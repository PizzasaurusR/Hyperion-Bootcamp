#-----------------------------------------------------------------------
# LIBRARY IMPORT
#-----------------------------------------------------------------------
import sqlite3

from models import Category, Transaction, Expense, User
from database import BudgetManager
from auth import login, register
#-----------------------------------------------------------------------
# CLASSES
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------

def main():
    '''
    Main function of the program.

    Main menu is based on menu used in previous bookstore_management
    program and integrated into main function.

    Changed Expense to Transaction for clarity. An expense should be 
    something that can be added ahead of time, such as Rent, and this 
    should be calculated into the ongoing budget.

    A transaction will be any deduction in funds that would occur in a
    persons day-to-day life, such as Groceries, Petrol etc.
    '''
    budget_manager = BudgetManager()

    print("--- Welcome to Budget Manager ---")
    while True:
        print("1. Login")
        print("2. Register")
        choice = input("Please choose an option: ")

        if choice == '1':
            user_id = login(budget_manager)
            break

        elif choice == '2':
            register(budget_manager)

        else:
            print("Invalid choice. Please try again.")   
    
    while True:
        print('''--- Budget Management Menu ---
            1. Add Transaction
            2. View Transactions
            3. View Transactions by Category
            4. Add Expense
            5. View Expenses
            6. Add Income
            7. View Income
            8. View Income by Category
            9. Set Budget for a Category
            10. View Budget for a Category
            11. Set Financial Goals
            12. View Progress Towards Financial Goal
            13. Quit''')
        choice = input("Please enter your choice: ")

        if  choice == '1':
            add_transaction(budget_manager, user_id)
        elif choice == '2':
            view_transactions(budget_manager, user_id)
        elif choice == '3':
            view_transactions_by_category(budget_manager, user_id)
        elif choice == '4':
            add_expense(budget_manager, user_id)
        elif choice == '5':
            view_expenses(budget_manager)
        elif choice == '6':
            add_income(budget_manager, user_id)
        elif choice == '7':
            view_income(budget_manager, user_id)
        elif choice == '8':
            view_income_by_category(budget_manager, user_id)
        elif choice == '9':
            set_budget_for_category(budget_manager)
        elif choice == '10':
            view_budget_for_category(budget_manager)
        elif choice == '11':
            set_financial_goals(budget_manager)
        elif choice == '12':
            view_progress_towards_goals(budget_manager)
        elif choice == '13':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again")


#-----------------------------------------------------------------------
# MAIN PROGRAM
#-----------------------------------------------------------------------