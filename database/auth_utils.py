import bcrypt
import mysql.connector
from mysql.connector import Error
from db_config import DB_CONFIG

def create_connection():
    """Establish a database connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error: '{e}' occurred while connecting to the database.")
        return None


def validate_user_login(email, password):
    """
    Validate a user's login credentials.

    Returns:
        - user_id (int): If login is successful, returns the user's ID.
        - None: If login fails.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            # Retrieve user details by email
            cursor.execute(
                "SELECT user_id, password_hash FROM Users WHERE email = %s",
                (email,)
            )
            user = cursor.fetchone()

            if user and bcrypt.checkpw(password.encode("utf-8"), user["password_hash"].encode("utf-8")):
                print(f"Login successful for user ID {user['user_id']}!")
                return user["user_id"]  # Return user_id on successful login
            else:
                print("Invalid email or password.")
                return None
        except Error as e:
            print(f"Error: '{e}' occurred during login validation.")
            return None
        finally:
            cursor.close()
            connection.close()
