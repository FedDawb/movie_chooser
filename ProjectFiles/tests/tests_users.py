import unittest
from ProjectFiles.users import Users
import re

# using this file to test and check if the Users class works correctly
# creating TestingUsersCls with checks for users being set up
# using setUp method to create mock user:
# so that the Users class attributes are established and then can be used/referenced in the unittests


class TestUsersCls(unittest.TestCase):
    def setUp(self):
        self.user = Users(user_id=1, email="tasian@gmail.com", username="Tasian1", age=25, password="123456")

# test to check that the users saved password is the hashed one (UTF-8) and not the user input string
    def test_password_is_hashed(self):
        self.assertNotEqual(self.user.password, "123456")
        self.assertIsInstance(self.user.password, bytes)

# test to check that the users email address is entered in the valid format according to the Users class using regex
    def test_email_is_valid(self):
        email_regex = r"^[a-zA-Z0-0_.+-]+@[a-zA-Z0-0-]+\.[a-zA-Z0-9-.]+$"
        self.assertRegex(self.user.email, email_regex)

    # def test_user_added_favourite(self):


# self.user.password is referencing details of user1 in setUP to run the test successfully


# user2 = Users(2, "nutters@gmail.com", "Nutmeg", 2, "badger")
# print(user1.user_id, user1.username)


if __name__ == "__main__":
    unittest.main()
