from flask import Blueprint, request, jsonify, session
from backend.app.services.students_service import (
    fetch_students, create_student, update_student, delete_student)

students_bp = Blueprint("students", __name__, url_prefix="/students")


def is_logged_in():
    return "user_id" in session


@students_bp.route("", methods=["GET"])
def get_students():
    if not is_logged_in():
        return jsonify({"error": "Unauthorized"}), 401

    sort = request.args.get("sort", "created_desc")
    students = fetch_students(sort)

    return jsonify(students), 200


@students_bp.route("", methods=["POST"])
def add_student():
    if not is_logged_in():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(silent=True) or {}

    sname = data.get("sname")
    age = data.get("age")
    course = data.get("course")

    if not sname or not age or not course:
        return jsonify({"error": "Invalid input data"}), 400

    try:
        create_student({
            "sname": sname.strip(),
            "age": int(age),
            "course": course.strip()
        })
        return jsonify({"message": "Student added successfully"}), 201
    except Exception:
        return jsonify({"error": "Failed to add student"}), 500


@students_bp.route("/<int:student_id>", methods=["PUT"])
def edit_student(student_id):
    if not is_logged_in():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(silent=True) or {}

    if not all(k in data for k in ("sname", "age", "course")):
        return jsonify({"error": "Invalid input data"}), 400

    success = update_student(student_id, {
        "sname": data["sname"].strip(),
        "age": int(data["age"]),
        "course": data["course"].strip()
    })

    if not success:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student updated successfully"}), 200


@students_bp.route("/<int:student_id>", methods=["DELETE"])
def remove_student(student_id):
    if not is_logged_in():
        return jsonify({"error": "Unauthorized"}), 401

    if not delete_student(student_id):
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"}), 200
