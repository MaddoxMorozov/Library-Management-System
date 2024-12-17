import csv
import mysql.connector
from datetime import datetime

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",      
        password="19091977",  
        database="library"   
    )

def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books_issued (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id VARCHAR(255),
        student_name VARCHAR(255),
        book_id VARCHAR(255),
        book_name VARCHAR(255),
        issue_date DATE,
        return_date DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pending_books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id VARCHAR(255),
        student_name VARCHAR(255),
        book_id VARCHAR(255),
        book_name VARCHAR(255),
        issue_date DATE,
        status VARCHAR(255)  -- 'Pending' status for pending books
    )
    """)

def process_pending_books():
    db = connect_db()
    cursor = db.cursor()

    create_tables(cursor)

    with open('books_issued.csv', mode='r') as file:
        reader = csv.reader(file)
        records = list(reader)[1:] 

    for record in records:
        student_id, student_name, book_id, book_name, issue_date_str, return_date_str = record
        issue_date = datetime.strptime(issue_date_str, '%Y-%m-%d')
        return_date = None if return_date_str == "Pending" else datetime.strptime(return_date_str, '%Y-%m-%d')

        cursor.execute("""
        INSERT INTO books_issued (student_id, student_name, book_id, book_name, issue_date, return_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (student_id, student_name, book_id, book_name, issue_date, return_date))

        if return_date is None:
            cursor.execute("""
            INSERT INTO pending_books (student_id, student_name, book_id, book_name, issue_date, status)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (student_id, student_name, book_id, book_name, issue_date, "Pending"))

    db.commit()
    cursor.close()
    db.close()

    print("Pending books have been inserted into the database.")
    
process_pending_books()
