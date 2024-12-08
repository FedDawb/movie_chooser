import unittest
from unittest.mock import patch
import requests


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
        """ Below are the results returned from the API call.
        If multiple matches are found the results key will contain multiple dictionaries.
        """
        endpoint = "search/movie"
        params = {"query": title}
        return self.call_api(endpoint, params)
    

class TMDBTestCase(unittest.TestCase):
    def setUp(self):
        self.api_key = "MyApiKey"
        self.movie_id = 106
        self.tmdb = TMDB(self.api_key)
        self.api_result = {
          "page": 1,
          "results": [
            {
                "id" : self.movie_id,
                "name" : "Predator"
            }
          ],
          "total_pages": 1,
          "total_results": 1
        }

    def test__init__(self):
        """ Test for the TMDB class init method """
        self.assertEqual(self.tmdb.api_key, self.api_key)

    @patch("ProjectFiles.TMDB_API.TMDB.call_api")
    def test_search(self, mocked_call_api):
        """  Test to ensure the returned value from call_api is returned by this method and call_api is invoked with
            the expected URL
         """
        mocked_call_api.return_value = {
          "page": 1,
          "results": [
            {
              "adult": False,
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
              "video": False,
              "vote_average": 6.8,
              "vote_count": 29
            }
          ],
          "total_pages": 1,
          "total_results": 1
        }

        title = "Marcel the Shell with Shoes On, Three"
        result = self.tmdb.search(title)

        self.assertEqual(result, mocked_call_api.return_value)
        mocked_call_api.assert_called_with(f"search/movie?query={title}")

    @patch("ProjectFiles.TMDB_API.TMDB.call_api")
    def test_get_movie_details(self, mocked_call_api):
        """  Test to ensure the returned value from call_api is returned by this method and call_api is invoked with
            the expected URL
         """
        mocked_call_api.return_value = self.api_result

        result = self.tmdb.get_movie_details(self.movie_id)

        self.assertEqual(result, mocked_call_api.return_value)
        mocked_call_api.assert_called_with(f"movie/{self.movie_id}")

    @patch("ProjectFiles.TMDB_API.TMDB.call_api")
    def test_similar_movie(self, mocked_call_api):
        """  Test to ensure the returned value from call_api is returned by this method and call_api is invoked with
            the expected URL
         """
        mocked_call_api.return_value = self.api_result

        result = self.tmdb.similar_movie(self.movie_id)

        self.assertEqual(result, mocked_call_api.return_value)
        mocked_call_api.assert_called_with(f"movie/{self.movie_id}/similar")


if __name__ == '__main__':
    unittest.main()
