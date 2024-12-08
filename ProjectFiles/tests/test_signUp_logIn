import unittest
from unittest.mock import patch
from flask import Flask
import sys
import os

# Points to directory above the current directory (containing the app.py file)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ProjectFiles')))
from app import app  


class FlaskTestCase(unittest.TestCase):

    # create a test client
    def setUp(self):
        self.client = app.test_client()
        # disable flask logging during testing to make output less noisy meaning we can see the test results more clearly
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

    # delete the test client after the tests - clean up
    def tearDown(self):
        pass
    
    # Test if the sign up page loads
    def test_signup_page_loads(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign Up', response.data)

    # Test if the create user function works
    def test_signup_user_creation(self):
        with patch('database.db_utils.add_user') as mock_add_user:
            mock_add_user.return_value = True
            response = self.client.post('/create_user', data={
                'username': 'testuser',
                'password': 'testpassword'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Welcome', response.data)

    # Test if the login page loads
    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    # Test if the login function works
    def test_successful_login(self):
        with patch('database.auth_utils.validate_user_login') as mock_validate_user_login:
            mock_validate_user_login.return_value = 1
            response = self.client.post('/sign_in', data={
                'username': 'testuser',
                'password': 'testpassword'
            })
            self.assertEqual(response.status_code, 302)
            self.assertIn(b'Redirecting', response.data)

    # Test if the login function fails
    def test_unsuccessful_login(self):
        with patch('database.auth_utils.validate_user_login') as mock_validate_user_login:
            mock_validate_user_login.return_value = None
            response = self.client.post('/sign_in', data={
                'username': 'wronguser',
                'password': 'wrongpassword'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Login failed', response.data)

if __name__ == '__main__':
    unittest.main()
