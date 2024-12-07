def search_by_title(api, title):
    movie_id = None
    results = api.search(title=title)

    if results["total_results"] == 1:
        # Only one result found, this is the movie to get recommendations for
        movie_id = results["results"][0]["id"]

    return movie_id, results