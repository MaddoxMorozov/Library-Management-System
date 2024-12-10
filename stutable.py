import mysql.connector

def newstu():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="19091977",
        database="SchoolLibrary"
    )
    cursor = connection.cursor()
    
    name = input("Enter student name: ")
    student_class = input("Enter class: ")
    section = input("Enter section: ")
    
    query = "INSERT INTO student (name, class, section) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, student_class, section))
    connection.commit()
    

    connection.close()

newstu()
