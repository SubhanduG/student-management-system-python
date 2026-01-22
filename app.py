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
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    students = []

    for r in rows:
        students.append({
            "id": r["id"],
            "name": r["sname"],
            "age": r["age"],
            "course": r["course"]
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


if __name__ == "__main__":
    app.run(debug=True)
