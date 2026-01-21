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
    try:
        age = int(input("Enter age : "))
    except ValueError:
        print("Please enter a valid number.")
    course = input("Enter course : ")

    query = "INSERT INTO students (sname, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)

    cursor.execute(query, values)
    conn.commit()
    print("\nStudent added successfully")


def update_student():
    try:
        try:
            student_id = int(input("Enter student ID to update: "))
        except ValueError:
            print("Please enter a valid numeric ID number.")
            return

        try:
            cursor.execute(
                "SELECT id FROM students WHERE id = %s", (student_id,))
            result = cursor.fetchone()
            if result is None:
                print("\nStudent ID not found")
                return
        except Exception as e:
            print("Database error while checking student ID: ", e)
            return

        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Course")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            new_name = input("\nEnter new name: ")
            query = "UPDATE students SET sname = %s WHERE id = %s"
            values = (new_name, student_id)

        elif choice == "2":
            new_age = int(input("\nEnter new age: "))
            query = "UPDATE students SET age = %s WHERE id = %s"
            values = (new_age, student_id)

        elif choice == "3":
            new_course = input("\nEnter new course: ")
            query = "UPDATE students SET course = %s WHERE id = %s"
            values = (new_course, student_id)

        else:
            print("\nInvalid option.")
            return

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount > 0:
            print("\nStudent updated successfully.")
        else:
            print("\nStudent ID not found.")

    except ValueError:
        print("Invalid input. Please enter correct values.")
    except Exception as e:
        print("Error occurred while updating studens: ", e)


def delete_student():
    try:
        try:
            student_id = int(input("Enter student ID to delete: "))
        except ValueError:
            print("Please enter a valid numeric ID number.")

        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print("\nStudent deleted successfully.")
        else:
            print("\nStudent ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
    except Exception as e:
        print("Error occurred while deleting student: ", e)


def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("\nNo students found.")
    else:
        for student in students:
            print(student)


while True:
    print("\n---------- Student Management System ----------")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View Students")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("\n")
        add_student()
    elif choice == "2":
        print("\n")
        update_student()
    elif choice == "3":
        print("\n")
        delete_student()
    elif choice == "4":
        print("\n")
        view_students()
    elif choice == "5":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice. Please try again...")
