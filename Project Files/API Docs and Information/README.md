# Important information about the TMDB API

### Login credentials:
username: Tasian
password: CFGgroup2-24!

### Documentation:
General
https://developer.themoviedb.org/docs/getting-started

Session Info
https://developer.themoviedb.org/reference/authentication-how-do-i-generate-a-session-id

### API logos and attribution:
- We must use the TMDB logo in our site to attribute that we are using their API, the documentation was very clear on 
this and below is a link with info and the logo options they permit us to use.
https://www.themoviedb.org/about/logos-attribution

GET REQUEST - Top Popular Movie (landing page carousel)
https://api.themoviedb.org/3/movie/popular?api_key=7411413e79aba1afbb33df28e0532a6f
Example response:
{
      "adult": false,
      "backdrop_path": "/tElnmtQ6yz1PjN1kePNl8yMSb59.jpg",
      "genre_ids": [16, 12, 10751, 35],
      "id": 1241982,
      "original_language": "en",
      "original_title": "Moana 2",
      "overview": "After receiving an unexpected call from her wayfinding ancestors, Moana journeys alongside Maui and a new crew to the far seas of Oceania and into dangerous, long-lost waters for an adventure unlike anything she's ever faced.",
      "popularity": 7121.204,
      "poster_path": "/4YZpsylmjHbqeWzjKpUEF8gcLNW.jpg",
      "release_date": "2024-11-27",
      "title": "Moana 2",
      "video": false,
      "vote_average": 7.052,
      "vote_count": 154
    }

GET REQUEST - Movie Lists by Genre
https://api.themoviedb.org/3/genre/movie/list?api_key=7411413e79aba1afbb33df28e0532a6f
Example response:
 {
      "id": 28,
      "name": "Action"
    }

GET REQUEST - Find Movies by 30 Filter and Sort Options 
https://api.themoviedb.org/3/discover/movie?api_key=7411413e79aba1afbb33df28e0532a6f
Example response is same as Top Popular Movies 


POST REQUEST - Add Movies to a List 
link to documentation on this:
https://developer.themoviedb.org/reference/list-add-movie

____

## Process Flow: Get Movie

### Find movie
Call search endpoint with movie name to obtain movie_id
```https://api.themoviedb.org/3/search/movie?query={movie_title}```

Call endpoint for movie detail with movie_id to fetch extended details, for example the budget, imdb_if, 
production companies, revenue, run time, tagline and lagnuages.
```https://api.themoviedb.org/3/movie/{movie_id}```
ref
https://developer.themoviedb.org/reference/movie-details

### Image
Images can be served by using the following URL followed by the ```poster_path``` or 
```backdrop_path```
```https://image.tmdb.org/t/p/original```

Additional images can be fetched  by the image endpoint
```https://api.themoviedb.org/3/movie/{movie_id}/images```

Reference 
```https://developer.themoviedb.org/reference/movie-images```

## Process Flow: Recommendations
### Recommendations
Appears to give decent results
```https://api.themoviedb.org/3/movie/{movie_id}/recommendations```

### Similar movies
Returns results with a similar genre and keywords.  Can be inaccurate
```https://api.themoviedb.org/3/movie/{movie_id}/similar```

### Genre Search
Advanced search, can be used to search across genre and age ratings
```https://api.themoviedb.org/3/discover/movie```

## Suggested Search Flow
1. User types in movie name on website
2. If more than 1 movie found then show top 20 movies and ask the user to confirm which movie they mean. STOP
3. Call recommendation endpoint using movie_id
4. Show recommendations to user

We need this for the single movie info page 
1. Otherwise, use movie_id from step 4 in and call "get movie details" endpoint