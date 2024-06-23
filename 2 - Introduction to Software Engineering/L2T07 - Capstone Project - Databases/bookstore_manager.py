#-----------------------------------------------------------------------
# LIBRARY IMPORT
#-----------------------------------------------------------------------
import sqlite3

#-----------------------------------------------------------------------
# CLASSES
#-----------------------------------------------------------------------
'''
Created class book. I thought it would be easier to have all the book
functions under the class rather than separate. This also lets the class
be used across the program and helps with modularity.

All methods are in try-except blocks for exception handling.
All methods specifically check for SQL errors - Thanks to Youtube.
All methods pass cursor object to make sure that the correct db is used.

All commits moved to class methods for cohesion. Also it made sense
because the changes are taking place inside these methods.
'''
class Book:
    def __init__(self, id, title, author, qty):  # Init object
        self.id = id
        self.title = title
        self.author = author
        self.qty = qty

    # Add a book to the database
    def add_book(self, cursor):
        try:
            cursor.execute('''
                INSERT INTO book (id, title, author, qty)
                VALUES (?, ?, ?, ?)
                ''', (self.id, self.title, self.author, self.qty))
            db.commit()
            print(f"{self.title} by {self.author} has been added "
                  f"successfully\n")
        except sqlite3.Error as error:
            # Rollback any changes
            if db:
                db.rollback()
            print(f"Error adding book {self.title}: {error}")


    # Update book in database
    def update_book(self, cursor):
        try:
            cursor.execute('''
                UPDATE book SET title = ?, author = ?, qty = ?
                WHERE id = ?
            ''', (self.title, self.author, self.qty, self.id))
            db.commit()
            print(f"Book with ID {self.id} updated successfully.")
        except sqlite3.Error as error:
            # Rollback any changes
            if db:
                db.rollback()
            print(f"Error updating book with ID {self.id}: {error}")


    @staticmethod
    # Delete book from database
    def delete_book(cursor, book_id):
        try:
            cursor.execute('''
                DELETE FROM book WHERE id = ?
            ''', (book_id,))
            db.commit()
            print(f"Book with ID {book_id} deleted successfully.")
        except sqlite3.Error as error:
            # Rollback any changes
            if db:
                db.rollback()
            print(f"Error deleting book with ID {book_id}: {error}")


    @staticmethod
    # Search for book in database
    def search_book(cursor, book_id):
        try:
            cursor.execute('''
                SELECT * FROM book WHERE id = ?
            ''', (book_id,))
            book = cursor.fetchone()

            if book:
                print(f"\nBook found:"
                      f"\nID: {book[0]}\nTitle: {book[1]}"
                      f"\nAuthor: {book[2]}\nQuantity: {book[3]}\n")
            else:
                print(f"No book with ID {book_id} found.")

        except sqlite3.Error as error:
            # Rollback any changes
            if db:
                db.rollback()
            print(f"Error searching for book {book_id}: {error}")


#-----------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------
'''
Menu was cluttered so I split each option into a function.

I got lazy with my error messages so now they just display the error.
'''

def database_init():
    '''
    Function to Initialize the Database.
    1 - The function will attempt to connect to or create the database
    2 - The function will check for data in the table and if empty it 
    will auto populate 
    '''
    try:
        # Create or open file called student.db
        db = sqlite3.connect('ebookstore.db')
        # Create cursor object
        cursor = db.cursor() 

        # Create a table called python_programming if it doesn't exist
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS
                book (
                id INTEGER PRIMARY KEY, 
                title TEXT, 
                author TEXT,
                qty INTEGER)    
        ''')

        # Check if table already has data
        cursor.execute('''
            SELECT COUNT(*) FROM book
        ''')
        table_count = cursor.fetchone()[0]

        # Insert given data in list format if table is empty
        if table_count == 0:
        
            default_book_data = [
        (3001, "A Tale Of Two Cities", "Charles Dickens", 30),
        (3002, "Harry Potter and the Philosipher's Stone", "J.K. Rowling", 40),
        (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
        (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
        (3005, "Alice in Wonderland", "Lewis Carroll", 12)
        ]

            # Insert data into table
            cursor.executemany('''
                INSERT INTO book (id, title, author, qty)
                VALUES (?, ?, ?, ?)
            ''', default_book_data)

            # Commit the changes
            db.commit()
        # Return db and cursor for use in rest of program
        return db, cursor

    # This code was taken from my previous exercise. It works well.
    except Exception as error:
        # Rollback any changes and return None
        if db:
            db.rollback()
        print(f"An error has occurred during database initialization. "
              f"Error: {error}")
        return None, None


def add_book(cursor):
    '''
    This function will gather inputs to gather book details when adding
    a new book to the table.
    After inputs are gathered, a new book object is created and then the 
    add_book method is called to insert the new object into the table.
    '''
    try:
        # Get input for book details
        print("\n--- Enter Book Details ---")
        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        qty = int(input("Enter quantity: "))

        # Create new_book object
        new_book = Book(book_id, title, author, qty)
        # Call add_book to add new book 
        new_book.add_book(cursor)
    
    except ValueError as error:
        print(f"Invalid input. Please try again: {error}.")
    
    except sqlite3.Error as error:
        print(f"Database error. Please try again: {error}")


def update_book(cursor):    
    '''
    So I wanted the search function to work a bit better. I added a 
    check to see if the book exists. If it does then the user is 
    prompted to enter the new information. 
    I made it so that leaving the input blank will just keep the 
    existing data. I learnt this on w3schools.  
    '''
    try:
        print("\n--- Update Book ---")
        book_id = int(input("Enter ID of the book to update: "))

        # Get all information of searched book
        cursor.execute('''
            SELECT * FROM book WHERE id = ?
        ''', (book_id,))
        existing_book = cursor.fetchone()

        # Get new information to update. Leave blank to keep as is.
        if existing_book:
            print("Please enter the new information or "
                  "leave blank to keep as is.\n")
            title = input(f"Enter new title (current: "
                          f"{existing_book[1]}): ").strip() or existing_book[1]
            author = input(f"Enter new author (current: "
                           f"{existing_book[2]}): ").strip() or existing_book[2]
            qty = int(input(f"Enter new quantity (current: "
                            f"{existing_book[3]}): "
                            "").strip() or existing_book[3])

            updated_book = Book(book_id, title, author, qty)
            updated_book.update_book(cursor)

        else:
            print(f"Book with ID {book_id} not found.")

    except ValueError as error:
        print(f"Invalid input: {error}")
    
    except sqlite3.Error as error:
        # Rollback any changes
            if db:
                db.rollback()
            print(f"Error updating book with ID {book_id}: {error}")


def delete_book(cursor):
    '''
    Main purpose of this function is to gather the ID of the book that 
    needs to be deleted.
    Function will get confirmation of deletion from the user.
    Once confirmed, the function calls the delete_book method to remove
    the book from the table.
    '''
    try:
        print("\n--- Delete Book ---")
        book_id = int(input("Enter ID of the book to delete: "))

        # Confirm delete
        confirm = input(f"Are you sure you want to delete book with ID "
                        f"{book_id}? (Y/N)\n:").lower()
        if confirm == 'y':
            Book.delete_book(cursor, book_id)

        else:
            print("Deletion cancelled. Returning to menu.")

    except ValueError as error:
        print(f"Invalid input. Please try again: {error}")

    except sqlite3.Error as error:
        # Rollback any changes
            if db:
                db.rollback()
            print(f"Error deleting book with ID {book_id}: {error}")


def search_book(cursor):
    '''
    This function gathers the input from the user to search for a book.
    Once the book_id has been received, the function will call the
    search_book method to find the book and its information.
    '''
    try:
        print("\n--- Search Book ---")
        book_id = int(input("Enter ID of the book to search: "))
        Book.search_book(cursor, book_id)

    except ValueError as error:
        print(f"Invalid input. Please try again: {error}")
    
    except sqlite3.Error as error:
        # Rollback any changes
            if db:
                db.rollback()
            print(f"Error searching for book {book_id}: {error}")


def exit_program():
    '''
    Just confirms exit option
    '''
    exit_app = input("Would you like to exit? (Y/N): ").lower()
    return exit_app == 'y'


def menu():
    '''
    Main menu function of the program.

    Had to set db and cursor as global or else they could not be
    accessed properly across the program.

    This also means that I can use these vars inside of a function
    without explicitly passing them as arguments. Not sure if this is 
    best practice but its the only way I managed to get this program to 
    work the way I wanted it to.
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
            1. Enter book
            2. Update book
            3. Delete book
            4. Search books
            0. Exit''')

            choice = input("Please enter your choice: ")

            if choice == '1':
                add_book(cursor)
            elif choice == '2':
                update_book(cursor)
            elif choice == '3':
                delete_book(cursor)
            elif choice == '4':
                search_book(cursor)
            elif choice == '0':
                if exit_program():
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
'''
This application can be used to manage stock in a bookstore.
Database and table are created on startup.
User has the option to Add, Update, Delete or Search for books.
'''
menu()