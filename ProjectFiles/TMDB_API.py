import requests

# This file will be used to house the API calls and the relevant urls to manage:
# searching for films
# returning details
# finding matches etc


class TMDB:
    base_url = "https://api.themoviedb.org/3/"  # all the URLs used below use the same starting point

    def __init__(self, api_key: str):
        self.api_key = api_key

    def call_api(self, endpoint: str, params: dict = None) -> dict:
            if params is None:
                params = {}
            params['api_key'] = self.api_key
            url = f"{self.base_url}{endpoint}"
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
    
    def search(self, title: str) -> dict:
        # If multiple matches are found the results key will contain multiple dictionaries.
        endpoint = "search/movie"
        params = {"query": title}
        return self.call_api(endpoint, params)

    def get_movie_details(self, movie_id: int) -> dict:
        endpoint = f"movie/{movie_id}"
        return self.call_api(endpoint)

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

    # api-certifications
    # def age_certifications(self, certification):
    #     url = f"{certification}/movie/list"
    #     response = requests.get(url)
    #     certifications = response.json()["certifications"]["GB"]  # should return the certifications from the GB array
    #     return self.call_api(url)

    def call_api(self, url: str) -> dict:
        """ This is the actual API call wth the api_key, need to import the API key from the protected//secret file

        """
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(f"{self.base_url}{url}", headers=headers)
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()

    # updating-age-certification-filtering
        response = requests.get(url, params={"api_key": self.api_key})
        if response.status_code == 200:
            country = "GB"  # Define the country variable
            certifications = response.json().get("certifications", {}).get(country, [])
            gb_certifications = {cert.get("certification") for cert in certifications}
            return gb_certifications
        else:
            response.raise_for_status()  # raising exception if the request fails

    def age_certifications(self, certification):
        url = f"{self.base_url}/certification/{certification}/movie/list"
        response = requests.get(url, params={"api_key": self.api_key})

        if response.status_code == 200:
            country = "GB"
            certifications = response.json().get("certifications", {}).get(country, [])
            gb_certifications = {cert.get("certification") for cert in certifications}
            return gb_certifications
        else:
            response.raise_for_status()  # raising exception if the request fails
