CREATE DATABASE db_movie_night;

USE db_movie_night;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(250) NOT NULL UNIQUE,
    preferences JSON, -- Stores genres, actors, etc.
    age INT NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE,
    password_hash VARCHAR(250) NOT NULL
);

-- api_id has been used for the movie identifier
CREATE TABLE User_Items (
    user_item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    api_id VARCHAR(250) NOT NULL, -- Unique ID from the API
    watched_date DATE,
    liked BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE TABLE Blocked_Items (
    blocked_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    api_id VARCHAR(250) NOT NULL, -- Unique ID from the API
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE TABLE Favourites (
    favourite_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    api_id VARCHAR(250) NOT NULL, -- Unique ID from the API
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Automatically stores the date when added
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);



