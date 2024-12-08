import unittest
from unittest.mock import patch
from decouple import config
import sys
import os

# Add the parent directory to the sys.path list
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TMDB_API import TMDB  # Ensure the correct import path

# The TMDB class is used to interact with the TMDB API.
class TMDBTestCase(unittest.TestCase):
    # The setUp method is called before each test in this class.
    def setUp(self):
        self.api_key = config("API_KEY")
        self.movie_id = 106
        self.tmdb = TMDB(self.api_key)
        self.api_result = {
            "page": 1,
            "results": [
                {
                    "id": self.movie_id,
                    "name": "Predator"
                }
            ],
            "total_pages": 1,
            "total_results": 1
        }

    # The tearDown method is called after each test in this class.
    def test__init__(self):
        """ Test for the TMDB class init method """
        self.assertEqual(self.tmdb.api_key, self.api_key)

    # The patch decorator is used to mock the call_api method of the TMDB class.
    @patch("TMDB_API.TMDB.call_api")
    def test_search(self, mocked_call_api):
        # The return value of the call_api method is set to the expected value.
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
        mocked_call_api.assert_called_with("search/movie", {"query": title})

    @patch("TMDB_API.TMDB.call_api")
    def test_get_movie_details(self, mocked_call_api):
        mocked_call_api.return_value = self.api_result

        result = self.tmdb.get_movie_details(self.movie_id)

        self.assertEqual(result, mocked_call_api.return_value)
        mocked_call_api.assert_called_with(f"movie/{self.movie_id}")

    @patch("TMDB_API.TMDB.call_api")
    def test_similar_movie(self, mocked_call_api):
        mocked_call_api.return_value = self.api_result

        result = self.tmdb.similar_movie(self.movie_id)

        self.assertEqual(result, mocked_call_api.return_value)
        mocked_call_api.assert_called_with(f"movie/{self.movie_id}/similar")


if __name__ == '__main__':
    unittest.main()
