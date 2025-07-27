# db_config.py
from decouple import config

# This dictionary now reads all its values from the .env file
# using the 'decouple' library.
#
# By adding a 'default' value, we prevent the application from crashing
# if a variable is not found in the .env file. This makes debugging much easier.
DB_CONFIG = {
    'user': config('DB_USER', default='root'),
    'password': config('DB_PASSWORD', default=''),
    'host': config('DB_HOST', default='localhost'),
    'port': config('DB_PORT', default='3306'),
    'database': config('DB_DATABASE', default='db_movie_night'),
}


