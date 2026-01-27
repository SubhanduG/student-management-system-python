from flask import Blueprint, request, jsonify, session
from backend.app.services.auth_service import (
    create_user, authenticate_user, reset_password
)

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    try:
        create_user(username, password)
        return jsonify({"message": "Registration successful"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = authenticate_user(username, password)
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    session["user_id"] = user["id"]
    return jsonify({"message": "Login successful"}), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"}), 200


@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    new_password = data.get("new_password")

    if not username or not new_password:
        return jsonify({"error": "Username and new password are required"}), 400

    if reset_password(username, new_password):
        return jsonify({"message": "Password reset successful"}), 200

    return jsonify({"error": "Username not found"}), 404
