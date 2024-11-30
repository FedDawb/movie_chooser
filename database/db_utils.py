import mysql.connector
from mysql.connector import Error

# Database configuration
DB_CONFIG = {
    'host': 'localhost',  # Change to your database host
    'user': 'root',       # Change to your MySQL username
    'password': 'password',  # Change to your MySQL password
    'database': 'db_movie_night'  # Change to your database name
}

def create_connection():
    """
    Establish a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        if connection.is_connected():
            print("Connection to the database was successful!")
            return connection
    except Error as e:
        print(f"Error: '{e}' occurred while connecting to the database.")
        return None

def execute_query(query, params=None):
    """
    Execute a single SQL query.
    :param query: The SQL query to execute.
    :param params: Optional parameters for the query.
    :return: None
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error: '{e}' occurred during query execution.")
        finally:
            cursor.close()
            connection.close()

def fetch_query(query, params=None):
    """
    Fetch results from a SELECT SQL query.
    :param query: The SQL query to execute.
    :param params: Optional parameters for the query.
    :return: List of results
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: '{e}' occurred during fetching.")
            return []
        finally:
            cursor.close()
            connection.close()
