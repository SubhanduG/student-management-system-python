from flask import Blueprint, request, jsonify, session
from backend.app.services.students_service import (
    fetch_students, create_student, update_student, delete_student)

students_bp = Blueprint("students", __name__, url_prefix="/students")


def login_required():
    return "user_id" in session


@students_bp.route("", methods=["GET"])
def get_students():
    if not login_required():
        return jsonify({"error": "Unauthorized"}), 401

    sort = request.args.get("sort", "created_desc")
    return jsonify(fetch_students(sort)), 200


@students_bp.route("", methods=["POST"])
def add_student():
    if not login_required():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    sname = data.get("sname")
    age = data.get("age")
    course = data.get("course")

    if not sname or not age or not course:
        return jsonify({"error": "invalid input data"}), 400

    create_student(data)
    return jsonify({"message": "Student added successfully"}), 201


@students_bp.route("/<int:student_id>", methods=["PUT"])
def edit_student(student_id):
    if not login_required():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not update_student(student_id, data):
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student updated successfully."}), 200


@students_bp.route("/<int:student_id>", methods=["DELETE"])
def remove_student(student_id):
    if not login_required():
        return jsonify({"error": "Unauthorized"}), 401

    if not delete_student(student_id):
        return jsonify({"error": "Student not found."}), 404

    return jsonify({"message": "Student deleted successfully."}), 200
