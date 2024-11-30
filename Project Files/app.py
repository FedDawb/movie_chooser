from flask import Flask, render_template
# importing packages:
# importing flask class from flask package
# render template for testing
from test import Film


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
    film = Film()
    context = {
        "movies": film.fake_search_api(),
    }
    return render_template("index_2.html", **context)

@app.route("/links")
def links():
    context = {}
    return render_template("links_2.html", **context)

@app.route("/about_us")
def about_us():
    context = {}
    return render_template("about_us.html", **context)

@app.route("/chosen_movie")
def chosen_movie():
    context = {}
    return render_template("chosen_movie.html", **context)


# telling the script to run if running this file and using the debugger to ensure it runs correctly and if not it will
# tell us immediately

if __name__ == "__main__":
    app.run(debug=True)