#-----------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------

from database import BudgetManager
from auth import login, register
import menu_functions as menu

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

    All menu functions moved out of main and into menu_functions.py
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
            menu.add_transaction(budget_manager, user_id)
        elif choice == '2':
            menu.view_transactions(budget_manager, user_id)
        elif choice == '3':
            menu.view_transactions_by_category(budget_manager, user_id)
        elif choice == '4':
            menu.add_expense(budget_manager, user_id)
        elif choice == '5':
            menu.view_expenses(budget_manager, user_id)
        elif choice == '6':
            menu.add_income(budget_manager, user_id)
        elif choice == '7':
            menu.view_income(budget_manager, user_id)
        elif choice == '8':
            menu.view_income_by_category(budget_manager, user_id)
        elif choice == '9':
            menu.set_budget_for_category(budget_manager, user_id)
        elif choice == '10':
            menu.view_budget_for_category(budget_manager, user_id)
        elif choice == '11':
            menu.set_financial_goals(budget_manager, user_id)
        elif choice == '12':
            menu.view_progress_towards_goals(budget_manager, user_id)
        elif choice == '13':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again")

    budget_manager.close()

