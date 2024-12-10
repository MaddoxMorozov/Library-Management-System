import mysql.connector

def createdb():
    connection = mysql.connector.connect(
        host="localhost",       
        user="root",   
        password="19091977" 
    )
    cursor = connection.cursor()
 
    cursor.execute("CREATE DATABASE IF NOT EXISTS SchoolLibrary")

    cursor.execute("USE SchoolLibrary")

    student_table = """
    CREATE TABLE IF NOT EXISTS student (
        student_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        class VARCHAR(50),
        section CHAR(1)
    )
    """
    cursor.execute(student_table)

    library_table = """
    CREATE TABLE IF NOT EXISTS library (
        library_id INT PRIMARY KEY AUTO_INCREMENT,
        student_id INT,
        book_name VARCHAR(200),
        return_date DATE,
        FOREIGN KEY (student_id) REFERENCES student(student_id)
    )
    """
    cursor.execute(library_table)

    connection.close()
createdb()
