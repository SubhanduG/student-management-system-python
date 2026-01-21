from flask import Flask, request, jsonify
from db_config import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return "Backend API is running"


@app.route("/students", methods=["GET"])
def get_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(students), 200


@app.route("/students", methods=["POST"])
def add_student_api():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    if not name or not age or not course:
        return jsonify({"error": "invalid input data"}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO students (sname, age, course) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, age, course))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
