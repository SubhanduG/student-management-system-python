# Student Management System
#
# 1. Connect to MySQL database
# 2. Show menu:
#    a) Add student
#    b) View students
#    c) Delete student
# 3. Take user unput
# 4. Perform database operation

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="student_db"
)

cursor = conn.cursor()
print("Connected to database")


def add_student():
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    course = input("Enter course : ")

    query = "INSERT INTO students (sname, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)

    cursor.execute(query, values)
    conn.commit()
    print("Student added successfully")


def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)


add_student()
view_students()
