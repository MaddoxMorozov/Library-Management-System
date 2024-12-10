import mysql.connector
import csv
from datetime import date

def pending_books():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="19091977",
        database="SchoolLibrary"
    )
    cursor = connection.cursor()
    
    query = """
        SELECT s.student_id, s.name, l.book_name, l.return_date
        FROM student s
        JOIN library l ON s.student_id = l.student_id
        WHERE l.return_date < CURDATE()
    """
    cursor.execute(query)
    results = cursor.fetchall()
    
    with open("pending_books.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Name", "Book Name", "Return Date"])
        writer.writerows(results)
    

    connection.close()

pending_books()
