def search_by_title(api, title):
    movie_id = None
    results = api.search(title=title)

    # Safely check if 'results' is not empty and if 'total_results' exists
    if results and results.get("total_results") == 1:
        # Only one result found, this is the movie to get recommendations for
        movie_id = results["results"][0]["id"]

    return movie_id, results