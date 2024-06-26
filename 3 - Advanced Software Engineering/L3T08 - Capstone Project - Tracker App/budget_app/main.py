#-----------------------------------------------------------------------
# LIBRARY IMPORT
#-----------------------------------------------------------------------
import sqlite3

#-----------------------------------------------------------------------
# CLASSES
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------

def quit_program():
    '''
    Exit program after confirmation
    '''
    exit_app = input("Would you like to exit? (Y/N): ").lower()
    return exit_app == 'y'

def menu():
    '''
    Main menu function of the program.

    Main menu is based on menu used in previous bookstore_management
    program.
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
            print('''--- Bookstore Management Menu ---
            1. Add Expense
            2. View Expenses
            3. View Expenses by Category
            4. Add Income
            5. View Income
            6. View Income by Category
            7. Set Budget for a Category
            8. View Budget for a Category
            9. Set Financial Goals
            10. View Progress Towards Financial Goal
            11. Quit''')

            choice = input("Please enter your choice: ")

            if choice == '1':
                add_expense(cursor)
            elif choice == '2':
                view_expense(cursor)
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
                if quit_program():
                    print("Exiting program. Goodbye!")
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