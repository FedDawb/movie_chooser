import re
import bcrypt

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
    def __init__(self, user_id, email, username, age, password, api):
        self.user_id = user_id
        self.email = email
        self.username = username
        self.age = age
        self.password = self.hash_password(password)  # bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
        self.api = api
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

    def check_email(self, email):
        valid_email = r"\b[A-Za-z0-9._%+-] +@[A-Z|a-z]{2,}\b"
        return re.match(valid_email, email)

    def filter_movies(self, movies):
        raise NotImplementedError


# creating an 18+ and <18 user subclass to filter what films are available to them based on their age at sign up
# def check_email(email):
#     valid_email = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
#     return re.match(valid_email, email)


# telling the subclasses that this should be implemented and raise an error if not


class Under18Users(Users):
    def __init__(self, user_id, email, username, age, password, api):
        if age >= 18:
            raise ValueError  # defining that a user with an age 18 or over does not belong in this Users subclass
        super().__init__(user_id, email, username, age, password, api)
        self.kids_certifications = {"U", "PG", "12A", "15"}

    def filter_movies(self, movies):
        filtered_movies = [
            movie for movie in movies
            if movie.get("certification") in self.kids_certifications
        ]
        return filtered_movies
    # returns the movies filtered based on <18 users attributes being satisfied

# starting to create the function to filter the films shown to the user based on if the user is 18+ or <18
# def filter_by_certification(user, movies):
#     filter_films = []
#     for film in films:
#         certification = film.get("certification")
#         if user.can_watch_film(certification):
#          u   filtered_films.


class Over18Users(Users):
    def __init__(self, user_id, email, username, age, password, api):
        if age < 18:
            raise ValueError  # defining that a user with an age under 18 does not belong in this Users subclass
        super().__init__(user_id, email, username, age, password, api)

    def filter_movies(self, movies):
        return movies

        # returns all the results to adult users, no filtering applies


def search_by_title(api, title):
    results = api.search_movies_by_title(title)  # or however the data is fetched

    print(results)  # Debugging step to inspect the structure of results

    if results and "total_results" in results:  # Check if the key exists
        if results["total_results"] == 1:
            movie_id = results["results"][0]["id"]  # or however the movie ID is accessed
            return movie_id, results["results"]  # returning the results as a list
    else:
        # Handle error or empty results gracefully
        return None, None
