/* This script creates 2 different users with 2 different databases */

-- Create users for SQL Authentication
CREATE USER 'airbnb_user_prod'@'localhost' IDENTIFIED BY '';
CREATE USER 'airbnb_user_dev'@'%' IDENTIFIED BY '';

-- Create 2 databases in UTF8 (utf8_general_ci)
CREATE DATABASE airbnb_dev CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE airbnb_prod CHARACTER SET utf8 COLLATE utf8_general_ci;

-- Add user dev to database dev
GRANT ALL PRIVILEGES ON database.airbnb_dev TO 'airbnb_user_dev'@'%' IDENTIFIED BY '';

-- Add user prod to database prod
GRANT ALL PRIVILEGES ON	database.airbnb_prod TO 'airbnb_user_prod'@'localhost' IDENTIFIED BY '';
