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
    def __init__(self, user_id, email, username, password):
        self.user_id = user_id
        self.email = email
        self.username = username
        self.password = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
        self.is_authenticated = False


# writing function to check the user password in check_password and feeding it password and hashpw from Users class
# unsure if this should be a method of the Users class or if it's ok to sit here
# my logic is that having it as a static method is better because it performs the task in isolation and won't be able to
# make changes to the class... maybe?

def check_password(self, password, hashpw):
    if hashpw == password:
        print("Welcome! Let's find your next film fix.")
        self.is_authenticated = True
    elif hashpw != password:
        print("Invalid password. ")
        return


def __str__(self, password, hashpw):
    print("We take our users privacy very seriously!")
    return


# for logging in with a self.is_authenticated = True (if statement?)

