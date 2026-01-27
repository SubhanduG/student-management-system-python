from database.db_config import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from mysql.connector import IntegrityError


def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, spassword) VALUES (%s, %s)",
            (username, generate_password_hash(password))
        )
        conn.commit()
    except IntegrityError:
        raise ValueError("Username already exists")
    finally:
        cursor.close()
        conn.close()


def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user and check_password_hash(user["spassword"], password):
            return user
        return None
    finally:
        cursor.close()
        conn.close()


def reset_password(username, new_password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if not user:
            return False
        cursor.execute(
            "UPDATE users SET spassword = %s WHERE username = %s",
            (generate_password_hash(new_password), username)
        )
        conn.commit()
        return True
    finally:
        cursor.close()
        conn.close()
