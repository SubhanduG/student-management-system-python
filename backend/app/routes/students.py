from flask import Blueprint, request, jsonify, session
from backend.app.services.students_service import (
    fetch_students, create_student, update_student, delete_student
)

students_bp = Blueprint("students", __name__, url_prefix="/students")


def is_logged_in():
    return "user_id" in session


@students_bp.route("", methods=["GET"])
def get_students():
    if not is_logged_in():
        return jsonify({"error": "Unauthorized"}), 401

    sort = request.args.get("sort", "created_desc")
    try:
        students = fetch_students(sort)
        return jsonify(students), 200
    except Exception:
        return jsonify({"error": "Failed to fetch students"}), 500


@students_bp.route("", methods=["POST"])
def add_student():
    if not is_logged_in():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(silent=True) or {}
    sname = data.get("sname", "").strip()
    age = data.get("age")
    course = data.get("course", "").strip()

    if not sname or not age or not course:
        return jsonify({"error": "All fields are required"}), 400

    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error": "Age must be a positive number"}), 400

    try:
        create_student({"sname": sname, "age": age, "course": course})
        return jsonify({"message": "Student added successfully"}), 201
    except Exception:
        return jsonify({"error": "Failed to add student"}), 500


@students_bp.route("/<int:student_id>", methods=["PUT"])
def edit_student(student_id):
    if not is_logged_in():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(silent=True) or {}
    sname = data.get("sname", "").strip()
    age = data.get("age")
    course = data.get("course", "").strip()

    if not sname or not age or not course:
        return jsonify({"error": "All fields are required"}), 400

    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error": "Age must be a positive number"}), 400

    try:
        success = update_student(
            student_id, {"sname": sname, "age": age, "course": course})
        if not success:
            return jsonify({"error": "Student not found"}), 404
        return jsonify({"message": "Student updated successfully"}), 200
    except Exception:
        return jsonify({"error": "Failed to update student"}), 500


@students_bp.route("/<int:student_id>", methods=["DELETE"])
def remove_student(student_id):
    if not is_logged_in():
        return jsonify({"error": "Unauthorized"}), 401

    try:
        if not delete_student(student_id):
            return jsonify({"error": "Student not found"}), 404
        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception:
        return jsonify({"error": "Failed to delete student"}), 500
