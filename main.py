# Student Management System
#
# 1. Connect to MySQL database
# 2. Show menu:
#    a) Add student
#    b) View students
#    c) Update student
#    d) Delete student
# 3. Take user unput
# 4. Perform database operation

from db_config import get_connection

conn = get_connection()
cursor = conn.cursor()
print("Connected to database")


def get_valid_int(message):
    try:
        value = input(message).strip()

        if value == "":
            print("Input cannot be empty.")
            return None

        number = int(value)
        return number

    except ValueError:
        print("Invalid Input. Please enter a valid numeric number.")
        return None
    except Exception as e:
        print("Unexpected error occurred: ", e)
        return None


def get_valid_string(message):
    try:
        value = input(message).strip()

        if value == "":
            print("Input cannot be empty.")
            return None

        return value

    except Exception as e:
        print("Unexpected error occurred: ", e)
        return None


def add_student():
    name = get_valid_string("Enter name : ")
    if name is None:
        return

    age = get_valid_int("Enter age : ")
    if age is None:
        return

    course = get_valid_string("Enter course : ")
    if course is None:
        return

    try:
        query = "INSERT INTO students (sname, age, course) VALUES (%s, %s, %s)"
        values = (name, age, course)
        cursor.execute(query, values)
        conn.commit()
        print("\nStudent added successfully")
    except Exception as e:
        print("Database error: ", e)


def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("\nNo students found.")
    else:
        for student in students:
            print(student)


def update_student():
    try:
        student_id = get_valid_int("Enter student ID to update: ")
        if student_id is None:
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
            new_name = get_valid_string("\nEnter new name: ")
            if new_name is None:
                return

            query = "UPDATE students SET sname = %s WHERE id = %s"
            values = (new_name, student_id)

        elif choice == "2":
            new_age = get_valid_int("Enter new age : ")
            if new_age is None:
                return

            query = "UPDATE students SET age = %s WHERE id = %s"
            values = (new_age, student_id)

        elif choice == "3":
            new_course = get_valid_string("\nEnter new course: ")
            if new_course is None:
                return

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
        student_id = get_valid_int("Enter student ID to delete: ")
        if student_id is None:
            return

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


while True:
    print("\n---------- Student Management System ----------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("\n")
        add_student()
    elif choice == "2":
        print("\n")
        view_students()
    elif choice == "3":
        print("\n")
        update_student()
    elif choice == "4":
        print("\n")
        delete_student()
    elif choice == "5":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice. Please try again...")
