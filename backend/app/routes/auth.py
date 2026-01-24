from flask import Blueprint, request, jsonify, session
from backend.app.services.auth_service import (
    create_user, authenticate_user, reset_password)

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)
    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Invalid input"}), 400

    try:
        create_user(data["username"], data["password"])
        return jsonify({"message": "Registration successful"}), 201
    except Exception as e:
        print("REGISTER ERROR:", e)
        return jsonify({"error": "Registration failed"}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    user = authenticate_user(data.get("username"), data.get("password"))

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    session["user_id"] = user["id"]
    return jsonify({"message": "Login successfully"}), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.pop("user_id", None)
    return jsonify({"message": "Logged out"}), 200


@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.json
    if not data.get("username") or not data.get("new_password"):
        return jsonify({"error": "Invalid input"}), 400

    if reset_password(data["username"], data["new_password"]):
        return jsonify({"message": "Password reset successful"}), 200
    return jsonify({"error": "Username not found"}), 404
