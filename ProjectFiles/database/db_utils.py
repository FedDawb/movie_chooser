import json
import bcrypt
from mysql.connector import connect, Error

from ProjectFiles.db_config import DB_CONFIG  # Import database configuration securely


def create_connection():
    """
    Create and return a database connection.
    """
    try:
        connection = connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error: '{e}' occurred while connecting to the database.")
        return None


# User-related functions
def add_user(email, username, password, age, preferences=None):
    """
    Add a new user to the Users table.
    """
    connection = create_connection()
    if connection:
        try:
            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Users (email, username, password_hash, age, preferences) 
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    email,
                    username,
                    hashed_password.decode("utf-8"),
                    age,
                    json.dumps(preferences or {}),
                ),
            )
            connection.commit()
            print(f"User '{username}' added successfully.")
        except Error as e:
            print(f"Error: '{e}' occurred while adding a user.")
        finally:
            cursor.close()
            connection.close()


def get_user_by_email(email):
    """
    Retrieve a user by their email.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Users WHERE email = %s", (email,))
            user = cursor.fetchone()
            return user
        except Error as e:
            print(f"Error: '{e}' occurred while retrieving user data.")
            return None
        finally:
            cursor.close()
            connection.close()


def update_user_preferences(user_id, preferences):
    """
    Update a user's preferences.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                UPDATE Users
                SET preferences = %s
                WHERE user_id = %s
                """,
                (json.dumps(preferences), user_id),
            )
            connection.commit()
            print(f"Preferences updated for user ID {user_id}.")
        except Error as e:
            print(f"Error: '{e}' occurred while updating preferences.")
        finally:
            cursor.close()
            connection.close()


# Movie-related functions
def save_favourite(user_id, api_id):
    """
    Save a movie or show as a favorite for a user.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)

            # Check if the movie/show is already a favorite
            cursor.execute(
                """
                SELECT * FROM Favourites 
                WHERE user_id = %s AND api_id = %s
                """,
                (user_id, api_id),
            )
            if cursor.fetchone():
                print(f"API ID {api_id} is already a favorite for user ID {user_id}.")
            else:
                # Add to favorites
                cursor.execute(
                    """
                    INSERT INTO Favourites (user_id, api_id)
                    VALUES (%s, %s)
                    """,
                    (user_id, api_id),
                )
                connection.commit()
                print(f"API ID {api_id} saved as a favorite for user ID {user_id}.")
        except Error as e:
            print(f"Error: '{e}' occurred while saving a favorite.")
        finally:
            cursor.close()
            connection.close()


def block_item(user_id, api_id):
    """
    Block a movie or show for a user.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Blocked_Items (user_id, api_id)
                VALUES (%s, %s)
                """,
                (user_id, api_id),
            )
            connection.commit()
            print(f"API ID {api_id} blocked for user ID {user_id}.")
        except Error as e:
            print(f"Error: '{e}' occurred while blocking an item.")
        finally:
            cursor.close()
            connection.close()


def delete_user(user_id):
    """
    Delete a user from the database.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM Users WHERE user_id = %s", (user_id,)
            )
            connection.commit()
            print(f"User ID {user_id} deleted successfully.")
        except Error as e:
            print(f"Error: '{e}' occurred while deleting a user.")
        finally:
            cursor.close()
            connection.close()
