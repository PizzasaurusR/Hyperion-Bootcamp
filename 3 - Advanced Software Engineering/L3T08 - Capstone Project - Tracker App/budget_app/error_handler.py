'''
Created this to consistently handle errors. This was in an attempt to 
make the program as modular as possible. I also got tired of adding
try-except blocks to every function. 

Thanks to stack overflow and youtube for help here.
Implemented rollbacks.
'''
#-----------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------

import functools
import sqlite3
from typing import Callable, Any

#-----------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------
def handle_db_errors(func: Callable):
    """
    Decorator to handle exceptions in database operations.
    """
    @functools.wraps(func)
    def wrapper_handle_db_errors(*args, **kwargs) -> Any:
        
        try:
            return func(*args, **kwargs)
        
        except sqlite3.IntegrityError as error:
            print(f"Integrity error: {error}")
            args[0].conn.rollback()

        except sqlite3.DatabaseError as error:
            print(f"Database error: {error}")
            args[0].conn.rollback()
        
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            args[0].conn.rollback()
    return wrapper_handle_db_errors

