import csv
from datetime import datetime

def inputstudentdata():
    records = []
    while True:
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        book_id = input("Enter book ID: ")
        book_name = input("Enter book name: ")
        issue_date_str = input("Enter issue date (YYYY-MM-DD): ")
        return_date_str = input("Enter return date (YYYY-MM-DD) or leave blank if not returned: ")
        
        try:
            issue_date = datetime.strptime(issue_date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid issue date format. Please use YYYY-MM-DD.")
            continue
        
        return_date = None
        if return_date_str.strip():  
            try:
                return_date = datetime.strptime(return_date_str, '%Y-%m-%d')
            except ValueError:
                print("Invalid return date format. Please use YYYY-MM-DD.")
                continue

        if not return_date:
            status = "Pending"
        else:
            status = "Returned"

        records.append([student_id, student_name, book_id, book_name, issue_date.strftime('%Y-%m-%d'), return_date.strftime('%Y-%m-%d') if return_date else "Pending"])

        more_data = input("Do you want to add another record? (y/n): ").lower()
        if more_data != 'y':
            break
        
    with open('books_issued.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student ID', 'Student Name', 'Book ID', 'Book Name', 'Issue Date', 'Return Date'])
        writer.writerows(records)
    print("Data has been saved to books_issued.csv")

inputstudentdata()
