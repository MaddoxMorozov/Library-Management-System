import mysql.connector

def newlib():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="19091977",
        database="SchoolLibrary"
    )
    cursor = connection.cursor()
    
    student_id = input("Enter student ID: ")
    book_name = input("Enter book name: ")
    return_date = input("Enter return date (YYYY-MM-DD): ")
    
    query = "INSERT INTO library (student_id, book_name, return_date) VALUES (%s, %s, %s)"
    cursor.execute(query, (student_id, book_name, return_date))
    connection.commit()
    
    connection.close()
newlib()
