CREATE DATABASE db_movie_night;

USE db_movie_night;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    preferences JSON -- Stores genres, actors, etc.
);

CREATE TABLE User_Items (
    user_item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    api_id VARCHAR(255) NOT NULL, -- Unique ID from the API
    watched_date DATE,
    liked BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE TABLE Blocked_Items (
    blocked_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    api_id VARCHAR(255) NOT NULL, -- Unique ID from the API
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

ALTER TABLE Users
ADD COLUMN age INT NOT NULL;



