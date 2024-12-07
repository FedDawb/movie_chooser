import math
from random import random
from decouple import config
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
# importing packages:
# importing flask class from flask package
# render template for testing
from TMDB_API import TMDB

import hashlib
from werkzeug.security import generate_password_hash

from search import search_by_title


#  This file will house Flask API code, manage routing and integrate with front-end
"""
route ideas
1. landing page
/ home

2. login page
/ login

3. displays list of favourite film(s)
/ faves

4. displays list of films based on user input(s)
/ user / search

5. enables user to add or remove a film on the favourites list
/ faves / edit (add/delete a fave film)
"""

# asking flask to use this file to run the request server side
app = Flask(__name__)

# app routing:
# the ROOT ADDRESS for our application is "/" our first function "home()" will manage the logic for the landing page
# using the app route decorator "app.route" binds the function and its logic to this root url
# running on port address http://127.0.0.1:5000/


# @app.route("/")
# def home():
#     context = {}
#     return render_template("base.html", **context)

@app.route("/") 
def home():
    api_key = config("API_KEY")
    api = TMDB(api_key)
    popular = api.popular_films()
    upcoming = api.upcoming_films()
    top_rated = api.top_rated()

    context = {
        "popular_movies": popular["results"],
        "upcoming_movies" : upcoming["results"],
        "top_rated" : top_rated["results"],
        "backdrop" : popular["results"][math.floor(random() * len(popular["results"]))]
    }
    return render_template("index_2.html", **context)

@app.route("/login", methods=[ 'GET', 'POST' ])
def login():
    if request.method == 'POST':
        # Check if the user exists in the database
        # 
        username = request.form.get('username')
        password = request.form.get('password')
        # Check password hash and compare with the one in the database
        #
        flash('Logged in successfully!', 'success')
        return redirect(url_for('home'))
   
    return render_template('login.html')

@app.route("/register", methods=[ 'GET', 'POST' ])
def sign_up():
    if request.method == 'POST' :
        email = request. form. get ( 'email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        if len(email) < 1:
            flash( 'Email must be greater than 0 characters.', category='error')
        elif len(firstName) < 1:
            flash( 'First name must be greater than 0 characters.', category='error')
        elif password1 != password2:
            flash( 'Passwords don\'t match.', category='error')
        elif len(password1) < 8:
            flash( 'Password must be at least 8 characters.', category='error')
        else:
            flash( 'Account created!', category='success')

        # Hash the password
            hashed_password = generate_password_hash(password1, method='sha256')
            
        # Save the user to your database here
            flash('Account created successfully!', 'success')
            return redirect(url_for("/login"))  # Redirect to login page after successful registration
    
    return render_template("register.html")

@app.route("/links")
def links():
    context = {}
    return render_template("links_2.html", **context)

@app.route("/about_us")
def about_us():
    context = {}
    return render_template("about_us.html", **context)

@app.route("/results", methods=["POST"])
def results():
    """Performs the search and shows the results"""
    # instantiating the TMDB class from TMDB_API.py which performs the search on the movie title from the data entered in the form
    api_key = config("API_KEY")
    api = TMDB(api_key)

    if request.form.get("search"):
        # Main search page after searching by title
        title = request.form.get("search")
        movie_id, results = search_by_title(api, title)
    else:
        # Searching on movie
        movie_id = request.form.get("movie_id")
        title = ""
        results = api.get_movie_details(movie_id)

    if movie_id:
        # 1 result fetch additional data
        context = {
            "movie_id": movie_id,
            "result": results["results"][0] if results.get("results") else results,
            "recommendations" : api.recommended_movie(movie_id)
        }
    elif results.get("results"):
        context = {"results": results["results"]}
    else:
        return render_template("not_found.html", search=title)

    return render_template("results.html", **context)


@app.route("/chosen_movie/<int:movie_id>")
def chosen_movie(movie_id):
    api_key = config("API_KEY")
    api = TMDB(api_key)
    context = {
        "movie": api.get_movie_details(movie_id),
        "reviews": api.reviews(movie_id),
        "actors": api.actors(movie_id),
        "provider" : api.provider(movie_id),
        "movie_videos" : api.movie_videos(movie_id),
        "recommendations": api.recommended_movie(movie_id)

    }
    return render_template("chosen_movie.html", **context)


@app.context_processor
def chosen_movie_processor():
    def actor_photo(person_id):
        api_key = config("API_KEY")
        api = TMDB(api_key)
        images = api.person_image(person_id)
        return images["profiles"][0] if images.get("profiles") and images["profiles"] else {}
    return dict(actor_photo=actor_photo)


@app.route("/actor/<int:person_id>")
def actor(person_id):
    api_key = config("API_KEY")
    api = TMDB(api_key)
    context = {
        "credits": api.movie_credits(person_id),
        "person": api.person_details(person_id),
    }
    return render_template("actor.html", **context)

# telling the script to run if running this file and using the debugger to ensure it runs correctly and if not it will
# tell us immediately

if __name__ == "__main__":
    app.run(debug=True)