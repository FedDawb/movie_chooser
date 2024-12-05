import json
import bcrypt
import mysql.connector
from mysql.connector import connect, Error
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
    """Validate a user's login credentials."""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT password_hash FROM Users WHERE email = %s",
                (email,)
            )
            user = cursor.fetchone()

            if user and bcrypt.checkpw(password.encode('utf-8'), user["password_hash"].encode('utf-8')):
                print("Login successful!")
                return True
            else:
                print("Invalid email or password.")
                return False
        except Error as e:
            print(f"Error: '{e}' occurred during login validation.")
            return False
        finally:
            cursor.close()
            connection.close()
