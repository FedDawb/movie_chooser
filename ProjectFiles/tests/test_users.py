import unittest
from unittest.mock import patch
from decouple import config
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from users import Users, Over18Users, search_by_title, api

class TestUsersCls(unittest.TestCase):
    def setUp(self):
        self.api_key = config("API_KEY")
        self.user = Users(user_id=1, email="tasian@gmail.com", username="Tasian1", age=25, password="123456", api=self.api_key)

    # test to check that the users saved password is the hashed one (UTF-8) and not the user input string
    def test_password_is_hashed(self):
        self.assertNotEqual(self.user.password, "123456")
        self.assertIsInstance(self.user.password, bytes)

    # test to check that the users email address is entered in the valid format according to the Users class using regex
    def test_email_is_valid(self):
        email_regex = r"^[a-zA-Z0-0_.+-]+@[a-zA-Z0-0-]+\.[a-zA-Z0-9-.]+$"
        self.assertRegex(self.user.email, email_regex)

    def test_over18_user_creation(self):
        over18_user = Over18Users(user_id=2, email="adult@gmail.com", username="AdultUser", age=30, password="password", api=self.api_key)
        self.assertEqual(over18_user.age, 30)

    def test_under18_user_creation(self):
        with self.assertRaises(ValueError):
            Over18Users(user_id=3, email="underage@gmail.com", username="UnderageUser", age=17, password="password", api=self.api_key)

    @patch("users.api.search_movies_by_title")
    def test_search_by_title(self, mock_search_movies_by_title):
        mock_search_movies_by_title.return_value = {
            "total_results": 1,
            "results": [
                {"id": 123, "title": "Test Movie"}
            ]
        }
        movie_id, results = search_by_title(api, "Test Movie")
        self.assertEqual(movie_id, 123)
        self.assertEqual(results[0]["title"], "Test Movie")

    @patch("users.api.search_movies_by_title")
    def test_search_by_title_no_results(self, mock_search_movies_by_title):
        mock_search_movies_by_title.return_value = {
            "total_results": 0,
            "results": []
        }
        movie_id, results = search_by_title(api, "Nonexistent Movie")
        self.assertIsNone(movie_id)
        self.assertIsNone(results)

if __name__ == '__main__':
    unittest.main()
