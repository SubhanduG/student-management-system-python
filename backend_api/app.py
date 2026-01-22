from flask import Flask, request, jsonify
from flask_cors import CORS
from db_config import get_connection

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Backend API is running"


@app.route("/students", methods=["GET"])
def get_students():
    sort = request.args.get("sort", "created_desc")

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

    students = []

    for r in rows:
        students.append({
            "id": r["id"],
            "name": r["sname"],
            "age": r["age"],
            "course": r["course"],
            "created_at": r["created_at"],
            "updated_at": r["updated_at"]
        })

    return jsonify(students), 200


@app.route("/students", methods=["POST"])
def add_student_api():
    data = request.get_json()

    sname = data.get("sname")
    age = data.get("age")
    course = data.get("course")

    if not sname or not age or not course:
        return jsonify({"error": "invalid input data"}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO students (sname, age, course) VALUES (%s, %s, %s)"
        cursor.execute(query, (sname, age, course))
        conn.commit()
        conn.close()

        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student_api(student_id):
    data = request.get_json()

    sname = data.get("sname")
    age = data.get("age")
    course = data.get("course")

    if not sname or not age or not course:
        return jsonify({"error": "invalid input data"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    cursor.execute("UPDATE students SET sname = %s, age = %s, course = %s WHERE id = %s",
                   (sname, age, course, student_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Student updated successfully."}), 200


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student_api(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Student not found."}), 404

    conn.close()
    return jsonify({"message": "Student deleted successfully."}), 200


if __name__ == "__main__":
    app.run(debug=True)
