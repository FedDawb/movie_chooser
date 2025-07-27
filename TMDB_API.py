import requests

# This file will be used to house the API calls and the relevant urls to manage:
# searching for films
# returning details
# finding matches etc


class TMDB:
    base_url = "https://api.themoviedb.org/3/"  # all the URLs used below use the same starting point

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(self, title: str) -> dict:
        url = f"search/movie?query={title}"
        return self.call_api(url)

    def get_movie_details(self, movie_id: int) -> dict:
        url = f"movie/{movie_id}"
        return self.call_api(url)

    def movie_videos(self, movie_id: int) -> dict:
        url = f"movie/{movie_id}/videos"
        return self.call_api(url)

    def similar_movie(self, movie_id: int) -> dict:
        url = f"movie/{movie_id}/similar"
        return self.call_api(url)

    def recommended_movie(self, movie_id: int) -> dict:
        url = f"movie/{movie_id}/recommendations"
        return self.call_api(url)

    def popular_films(self):
        url = "movie/popular?language=en-US&page=1"
        return self.call_api(url)

    def upcoming_films(self):
        url = "movie/upcoming"
        return self.call_api(url)

    def top_rated(self):
        url = "movie/top_rated"
        return self.call_api(url)

    def reviews(self, movie_id):
        url = f"movie/{movie_id}/reviews"
        return self.call_api(url)

    def actors(self, movie_id):
        url = f"movie/{movie_id}/credits"
        return self.call_api(url)

    def movie_credits(self, person_id):
        url = f"person/{person_id}/movie_credits"
        return self.call_api(url)

    def person_details(self, person_id):
        url = f"person/{person_id}"
        return self.call_api(url)

    def person_image(self, person_id):
        url = f"person/{person_id}/images"
        return self.call_api(url)

    def provider(self, movie_id):
        url = f"movie/{movie_id}/watch/providers"
        return self.call_api(url)

    def age_certifications(self):
        # Note: The 'certification' parameter was removed as it was not used.
        # This now fetches a general list of movie certifications.
        url = "certification/movie/list"
        return self.call_api(url)

    def call_api(self, url: str) -> dict:
        """
        This is the actual API call with the api_key.
        """
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        # This is the full, correct URL for the API request.
        full_url = f"{self.base_url}{url}"
        
        try:
            response = requests.get(full_url, headers=headers)
            # This will raise an exception for error status codes (4xx or 5xx).
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while calling the API: {e}")
            return {} # Return an empty dictionary on failure
