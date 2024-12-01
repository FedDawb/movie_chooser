import json
import bcrypt
import mysql.connector
from mysql.connector import connect, Error

# Database configuration
DB_CONFIG = {
    'host': 'localhost',  # Change to your database host
    'user': 'root',       # Change to your MySQL username
    'password': 'password',  # Change to your MySQL password
    'database': 'db_movie_night'  # Change to your database name
}

def create_connection():
    """
    Create and return a database connection.
    """
    try:
        connection = connect(
            host="localhost",        # Replace with your MySQL host
            user="your_user",        # Replace with your MySQL username
            password="your_password",# Replace with your MySQL password
            database="db_movie_night"# Replace with your database name
        )
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
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Users (email, username, password_hash, age, preferences) 
                VALUES (%s, %s, %s, %s, %s)
                """,
                (email, username, hashed_password.decode('utf-8'), age, json.dumps(preferences or {}))
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
            cursor.execute(
                "SELECT * FROM Users WHERE email = %s",
                (email,)
            )
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
                (json.dumps(preferences), user_id)
            )
            connection.commit()
            print(f"Preferences updated for user ID {user_id}.")
        except Error as e:
            print(f"Error: '{e}' occurred while updating preferences.")
        finally:
            cursor.close()
            connection.close()

# Movie-related functions
def add_movie(user_id, movie_id, title):
    """
    Save a movie to a user's favorites.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Favourites (user_id, movie_id, title)
                VALUES (%s, %s, %s)
                """,
                (user_id, movie_id, title)
            )
            connection.commit()
            print(f"Movie '{title}' added to user {user_id}'s favorites.")
        except Error as e:
            print(f"Error: '{e}' occurred while adding a movie.")
        finally:
            cursor.close()
            connection.close()

def block_item(user_id, movie_id):
    """
    Block a movie or show for a user.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Blocked_Items (user_id, movie_id)
                VALUES (%s, %s)
                """,
                (user_id, movie_id)
            )
            connection.commit()
            print(f"Movie ID {movie_id} blocked for user ID {user_id}.")
        except Error as e:
            print(f"Error: '{e}' occurred while blocking an item.")
        finally:
            cursor.close()
            connection.close()

def save_favourite(user_id, movie_id):
    """
    Save a movie or show as a favorite for a user.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)

            # Check if the movie is already a favorite
            cursor.execute(
                """
                SELECT * FROM Favourites 
                WHERE user_id = %s AND movie_id = %s
                """,
                (user_id, movie_id)
            )
            if cursor.fetchone():
                print(f"Movie ID {movie_id} is already a favorite for user ID {user_id}.")
            else:
                # Add to favorites
                cursor.execute(
                    """
                    INSERT INTO Favourites (user_id, movie_id)
                    VALUES (%s, %s)
                    """,
                    (user_id, movie_id)
                )
                connection.commit()
                print(f"Movie ID {movie_id} saved as a favorite for user ID {user_id}.")
        except Error as e:
            print(f"Error: '{e}' occurred while saving a favorite.")
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
                "DELETE FROM Users WHERE user_id = %s",
                (user_id,)
            )
            connection.commit()
            print(f"User ID {user_id} deleted successfully.")
        except Error as e:
            print(f"Error: '{e}' occurred while deleting a user.")
        finally:
            cursor.close()
            connection.close()
