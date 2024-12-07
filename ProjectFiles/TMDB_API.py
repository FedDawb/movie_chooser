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
        """ Below are the results returned from the API call.
        If multiple matches are found the results key will contain multiple dictionaries.

        {
          "page": 1,
          "results": [
            {
              "adult": false,
              "backdrop_path": "/xI5oKkOyu7H9Wm18C7U4oJYXIWo.jpg",
              "genre_ids": [
                35,
                16
              ],
              "id": 419474,
              "original_language": "en",
              "original_title": "Marcel the Shell with Shoes On, Three",
              "overview": "Marcel the shell gets locked outside.",
              "popularity": 3.328,
              "poster_path": "/2cYCWXDnvDIc7PiCOpXIfOf2uyu.jpg",
              "release_date": "2014-10-20",
              "title": "Marcel the Shell with Shoes On, Three",
              "video": false,
              "vote_average": 6.8,
              "vote_count": 29
            }
          ],
          "total_pages": 1,
          "total_results": 1
        }
        """
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

    def age_certifications(self, certification):
        url = f"{certification}/movie/list"
        response = requests.get(url)
        certifications = response.json()["certifications"]["GB"]  # should return the certifications from the GB array
        return self.call_api(url)

    def call_api(self, url: str) -> dict:
        """ This is the actual API call wth the api_key, need to import the API key from the protected//secret file

        """
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        result = requests.get(f"{self.base_url}{url}", headers=headers)
        return result.json()



