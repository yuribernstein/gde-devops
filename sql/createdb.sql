CREATE DATABASE Production;
USE Production;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    birth_date DATE,
    state VARCHAR(2) NOT NULL
);

CREATE TABLE Requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    zip_code VARCHAR(10),
    request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    weather_response TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- SAMPLE DATA
INSERT INTO Users (username, password, email, birth_date, state) VALUES 
('johndoe', 'hashed_password123', 'john.doe@example.com', '1990-01-01', 'CA'),
('janedoe', 'hashed_password321', 'jane.doe@example.com', '1992-02-02', 'NY'),
('aliceblue', 'hashed_password456', 'alice.blue@example.com', '1988-03-03', 'TX');

INSERT INTO Requests (user_id, zip_code, weather_response) VALUES
(1, '90210', 'Sunny with a high of 75 degrees'),
(1, '10001', 'Rainy with a high of 55 degrees'),
(2, '94105', 'Foggy with a high of 60 degrees'),
(3, '60601', 'Snowy with a high of 32 degrees'),
(3, '33101', 'Cloudy with a chance of thunderstorms');




CREATE DATABASE Testing;
USE Testing;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    birth_date DATE,
    state VARCHAR(2) NOT NULL
);

CREATE TABLE Requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    zip_code VARCHAR(10),
    request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    weather_response TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- SAMPLE DATA
INSERT INTO Users (username, password, email, birth_date, state) VALUES 
('johndoe', 'hashed_password123', 'john.doe@example.com', '1990-01-01', 'CA'),
('janedoe', 'hashed_password321', 'jane.doe@example.com', '1992-02-02', 'NY'),
('aliceblue', 'hashed_password456', 'alice.blue@example.com', '1988-03-03', 'TX');

INSERT INTO Requests (user_id, zip_code, weather_response) VALUES
(1, '90210', 'Sunny with a high of 75 degrees'),
(1, '10001', 'Rainy with a high of 55 degrees'),
(2, '94105', 'Foggy with a high of 60 degrees'),
(3, '60601', 'Snowy with a high of 32 degrees'),
(3, '33101', 'Cloudy with a chance of thunderstorms');

