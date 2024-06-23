import sqlite3

try:
    # Create or open file called student.db
    db = sqlite3.connect('student.db')
    # Create cursor object
    cursor = db.cursor() 

    # Create a table called python_programming if it doesn't exist
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS
               python_programming (
               id INTEGER PRIMARY KEY, 
               name TEXT, 
               grade INTEGER)    
    ''')
    
    # Create rows list to add insert into table
    new_rows = [
        (55, 'Carl Davis', 61),
        (66, 'Dennis Fredrickson', 88),
        (77, 'Jane Richards', 78),
        (12, 'Peyton Sawyer', 45),
        (2, 'Lucas Brooke', 99)
    ]

    # Insert into table
    cursor.executemany('''
        INSERT INTO python_programming (id, name, grade)
        VALUES (?, ?, ?)
    ''', new_rows)
    
    # Get all records with a grade between 60 and 80
    cursor.execute('''
        SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80        
        ''')
    
    # Fetch and print all results 
    student_grades = cursor.fetchall()
    print(student_grades)

    # Create Carl Davis grade update vars
    grade_update_name = 'Carl Davis'
    new_grade = 65

    # Update Carl Davis grade to 65
    cursor.execute('''
        UPDATE python_programming SET grade = ? WHERE name = ?
        ''', (new_grade, grade_update_name))
    
    # Create var to delete Dennis Fredrickson row
    delete_name = 'Dennis Fredrickson'

    cursor.execute('''
                   DELETE FROM python_programming WHERE name = ? 
                   ''', (delete_name,))
    
    # Update grade to 80 for students with id greater than 55
    cursor.execute('''
        UPDATE python_programming SET grade = 80 WHERE id > 55
    ''')
    
    # Sanity check by printing all rows
    cursor.execute('''
        SELECT * FROM python_programming
    ''')
    updated_rows = cursor.fetchall()
    print("Updated Records:")
    for row in updated_rows:
        print(row)
    
    # Commit the changes
    db.commit()

# Catch all exceptions as filler
except Exception as error:
    # Rollback any changes
    if db:
        db.rollback()
    print(f"An error has occurred. No changes have been made. Error: {error}")
finally:
    # Close connection
    if db:
        db.close()
