import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import DB_CONFIG
import mysql.connector
from mysql.connector import Error

class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=DB_CONFIG['host'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password'],
                database=DB_CONFIG['database'],
                port=DB_CONFIG['port']
            )
            self.assertTrue(connection.is_connected())
        except Error as e:
            self.fail(f"Database connection failed: {e}")
        finally:
            if connection and connection.is_connected():
                connection.close()

if __name__ == "__main__":
    unittest.main()
