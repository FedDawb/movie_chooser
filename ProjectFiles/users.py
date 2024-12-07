import re
import bcrypt
# import re

# importing BCrypt library to hash passwords and RegEx to validate user emails
# This file will be used to define our User class and authentication

# defining our Users class:
# has the attributes email, username and password which are defined in the object initialise-r
# using bcrypt library to hash user passwords before they are stored in our db and salts for during storage in db
# users password is therefore not stored in our db, only the hashed, salt version
# made an amendment so that the password attribute checks the hashed password (utf-8 version) and not the users password
# that's input into the password field
# self.is_authenticated used to flag when a user is logged in
# using "utf-8" encoder to translate string password into byte representation to leverage BCrypt library
# "bcrypt.gensalt()" ensures that a unique salt is created per user password


class Users:
    def __init__(self, user_id, email, username, age, password):
        self.user_id = user_id
        self.email = email
        self.username = username
        self.age = age
        self.password = self.hash_password(password)  # bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
        self.is_authenticated = False

# writing a function to hash and salt the users entered password function:
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
# check_password method updated because the previous code was trying to match between the hashed what the user entered:

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("UTF-8"), self.password)

# enabling the user to login once their password has been checked and the password matches between input and hashed:
    def login(self, password):
        if self.check_password(password):
            self.is_authenticated = True  # then the user has been authenticated
            return True  # the user entered a password that matches the hashed one
        return False  # the user entered a password that doesn't match the hashed one


def check_email(email):
    valid_email = r"\b[A-Za-z0-9._%+-] +@[A-Z|a-z]{2,}\b"
    return re.match(valid_email, email)

# creating an 18+ and <18 user subclass to filter what films are available to them based on their age at sign up


class Over18Users(Users):
    def can_watch_film(self, certification):
        return True


class Under18Users(Users):
    def __init__(self, user_id, email, username, age, password):
        super().__init__(user_id, email, username, age, password)

    def can_watch_film(self, certification):
        if certification == "18":
            return False  # ensures that only users who are 18 can have films rated 18 returned
        return True

# def __str__(self, password, hashpw):
#     print("We take our users privacy very seriously!")
#     return


