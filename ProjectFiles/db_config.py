from decouple import config

DB_CONFIG = {
    "host": config("DB_HOST", default=""),
    "user": config("DB_USER", default=""),
    "password": config("DB_PASSWORD", default=""),
    "database": config("DB_DATABASE", default=""),
}