#-----------------------------------------------------------------------
# LIBRARY IMPORT
#-----------------------------------------------------------------------
import sqlite3

from models import Category, Transaction, Expense
from database import BudgetManager
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
    # Call global vars and assign by initiating db  
    global db, cursor
    db, cursor = database_init()

    # Catch error
    if not db or not cursor:
        print("Failed to initialize database. Exiting program.")
        return

    # Display Menu
    try:
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

            if choice == '1':
                add_expense(cursor)
            
            elif choice == '2':
                budget_manager.view_transactions()

            elif choice == '3':
                view_expense_category(cursor)
            elif choice == '4':
                add_income(cursor)
            elif choice == '5':
                view_income(cursor)
            elif choice == '6':
                view_income_category(cursor)
            elif choice == '7':
                set_budget_category(cursor)
            elif choice == '8':
                view_budget_category(cursor)
            elif choice == '9':
                set_goals(cursor)
            elif choice == '10':
                view_progress(cursor)
            
            elif choice == '11':
                # Set Financial Goals logic
                pass
            elif choice == '12':
                # View Progress Towards Financial Goal logic
                pass
            elif choice == '13':
                budget_manager.close()
                break
            else:
                print("Invalid choice. Please enter a number from the menu.")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

    finally:
        if db:
            db.close()
#-----------------------------------------------------------------------
# MAIN PROGRAM
#-----------------------------------------------------------------------