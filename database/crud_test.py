import mysql.connector
import json
from mysql.connector import Error

# Database configuration
DB_CONFIG = {
    'host': 'localhost',  # Change as needed
    'user': 'root',       # Change as needed
    'password': 'password',  # Change as needed
    'database': 'db_movie_night'  # Change as needed
}

def create_connection():
    """Establish a database connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error: '{e}' occurred while connecting to the database.")
        return None

def add_user(username, age, preferences=None):
    """Add a new user to the Users table."""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Users (username, age, preferences) VALUES (%s, %s, %s)",
                (username, age, json.dumps(preferences or {}))
            )
            connection.commit()
            print(f"User '{username}' added successfully.")
        except Error as e:
            print(f"Error: '{e}' occurred while adding a user.")
        finally:
            cursor.close()
            connection.close()

def add_movie_show(title, genre=None, actors=None, director=None, release_year=None, type_="Movie"):
    """Add a new movie or show to the Movies_Shows table."""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Movies_Shows (title, genre, actors, director, release_year, type) VALUES (%s, %s, %s, %s, %s, %s)",
                (title, json.dumps(genre or []), json.dumps(actors or []), director, release_year, type_)
            )
            connection.commit()
            print(f"Movie/Show '{title}' added successfully.")
        except Error as e:
            print(f"Error: '{e}' occurred while adding a movie/show.")
        finally:
            cursor.close()
            connection.close()

def block_item(user_id, item_id):
    """Block a movie or show for a user."""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Blocked_Items (user_id, api_id) VALUES (%s, %s)",
                (user_id, item_id)
            )
            connection.commit()
            print(f"Item '{item_id}' blocked for user '{user_id}'.")
        except Error as e:
            print(f"Error: '{e}' occurred while blocking an item.")
        finally:
            cursor.close()
            connection.close()

def save_favourite(user_id, item_id):
    """Save a movie or show as a favorite for a user."""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # Fetch current favorites
            cursor.execute("SELECT preferences FROM Users WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
            if result:
                favourites = json.loads(result[0])

                # Add new favorite if not already present
                if item_id not in favourites:
                    favourites.append(item_id)
                    cursor.execute(
                        "UPDATE Users SET preferences = %s WHERE user_id = %s",
                        (json.dumps(favourites), user_id)
                    )
                    connection.commit()
                    print(f"Item '{item_id}' added to favorites for user '{user_id}'.")
                else:
                    print(f"Item '{item_id}' is already in favorites for user '{user_id}'.")
            else:
                print(f"User '{user_id}' not found.")
        except Error as e:
            print(f"Error: '{e}' occurred while saving a favorite.")
        finally:
            cursor.close()
            connection.close()

