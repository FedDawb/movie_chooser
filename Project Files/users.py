import bcrypt
# importing BCrypt library to hash passwords
# This file will be used to define our User class and authentication

# defining our Users class:
# has the attributes email, username and password which are defined in the object initialise-r
# using bcrypt library to hash user passwords before they are stored in our db and salts for during storage in db
# users password is therefore not stored in our db, only the hashed, salt version
# self.is_authenticated used to flag when a user is logged in
# using "utf-8" encoder to translate string password into byte representation to leverage BCrypt library
# "bcrypt.gensalt()" ensures that a unique salt is created per user password


class Users:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
        self.is_authenticated = False


# need to write:
# a function for checking the password
# and
# for logging in with a self.is_authenticated = True (if statement?)
