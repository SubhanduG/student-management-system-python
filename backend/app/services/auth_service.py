from database.db_config import get_connection
from werkzeug.security import generate_password_hash, check_password_hash


def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, spassword) VALUES (%s, %s)",
                   (username, generate_password_hash(password)))
    conn.commit()
    conn.close()


def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))

    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user["spassword"], password):
        return user
    return None


def reset_password(username, new_password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if not user:
        conn.close()
        return False

    cursor.execute("UPDATE users SET spassword = %s WHERE username = %s",
                   (generate_password_hash(new_password), username))
    conn.commit()
    conn.close()
    return True
