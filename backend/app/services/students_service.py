from database.db_config import get_connection


def fetch_students(sort):
    order_by = {
        "name": "sname ASC",
        "created_asc": "created_at ASC",
        "created_desc": "created_at DESC",
        "updated_desc": "updated_at DESC"
    }.get(sort, "created_at DESC")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM students ORDER BY {order_by}")
    rows = cursor.fetchall()
    conn.close()

    return [{
            "id": r["id"],
            "name": r["sname"],
            "age": r["age"],
            "course": r["course"],
            "created_at": r["created_at"],
            "updated_at": r["updated_at"]
            } for r in rows]


def create_student(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO students (sname, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (data["sname"], data["age"], data["course"]))
    conn.commit()
    conn.close()


def update_student(student_id, data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
    if cursor.fetchone() is None:
        conn.close()
        return False

    cursor.execute("UPDATE students SET sname = %s, age = %s, course = %s WHERE id = %s",
                   (data["sname"], data["age"], data["course"], student_id))
    conn.commit()
    conn.close()
    return True


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted
