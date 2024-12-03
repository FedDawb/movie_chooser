from decouple import config
from flask import Flask, render_template, request
# importing packages:
# importing flask class from flask package
# render template for testing
from api_example import Film
from TMDB_API import TMDB

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

# @app.route("/")
# def home():
#     api_key = config("API_KEY")
#     # film = Film()
#     context = {
#         # "movies": film.fake_search_api(),
#     }
#     return render_template("index_2.html", **context)

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
        "top_rated" : top_rated["results"]
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

@app.route("/login")
def login():
    context = {}
    return render_template("login.html", **context)

@app.route("/results", methods=["POST"])
def results():
    """Performs the search and shows the results"""
    api_key = config("API_KEY")

    # instantiating the TMDB class from TMDB_API.py which performs the search on the movie title from the data entered in the form
    api = TMDB(api_key)

    context = {}
    movie_id = None

    # Main search page after searching by title
    if request.form.get("search"):
        results = api.search(title=request.form.get("search"))
        if results["total_results"] > 1:
            # More than one result, therefore the user needs to select which film they meant
            context = {"results": results["results"]}
        else:
            # Only one result found, this is the movie to get recommendations for
            movie_id = results["results"][0]["id"]

    # The else is for when you have multiple results and we ask the user to pick which movie they meant
    else:
        movie_id = request.form.get("movie_id")
        results = api.get_movie_details(movie_id)

    if movie_id:
        # 1 result fetch additional data
        context = {
            "movie_id": movie_id,
            "result": results["results"][0] if results.get("results") else results,
            "recommendations" : api.recommended_movie(movie_id)
        }

    return render_template("results.html", **context)


# telling the script to run if running this file and using the debugger to ensure it runs correctly and if not it will
# tell us immediately

if __name__ == "__main__":
    app.run(debug=True)