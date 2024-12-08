from decouple import config

# Database configuration
DB_CONFIG = {
    "host": config("DB_HOST", default="localhost"),
    "user": config("DB_USER", default="root"),
    "password": config("DB_PASSWORD", default=""),
    "database": config("DB_NAME", default="db_movie_nights"),
    "port": config("DB_PORT", default="3306"),
}




