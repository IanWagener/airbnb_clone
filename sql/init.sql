/* This script creates 2 different users with 2 different databases */

-- Create users for SQL Authentication
CREATE LOGIN airbnb_user_dev WITH PASSWORD = 'notSuitableForGitHub', DEFAULT_DATABASE = [airbnb_dev]
GO
CREATE LOGIN airbnb_user_prod WITH PASSWORD = 'notSuitableForGitHub', DEFAULT_DATABASE = [airbnb_prod]
GO

-- Create 2 databases in UTF8 (utf8_general_ci)
CREATE DATABASE airbnb_dev CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE airbnb_prod CHARACTER SET utf8 COLLATE utf8_general_ci;

-- Add user dev to database dev
USE airbnb_dev;
CREATE USER airbnb_user_dev FOR LOGIN airbnb_user_dev;
EXEC sp_addrolemember 'db_datareader', 'airbnb_user_dev'
EXEC sp_addrolemember 'db_datawriter', 'airbnb_user_dev'
GO

-- Add user prod to database prod
USE airbnb_prod;
CREATE USER airbnb_user_prod FOR LOGIN airbnb_user_prod;
EXEC sp_addrolemember 'db_datareader', 'airbnb_user_prod'
EXEC sp_addrolemember 'db_datawriter', 'airbnb_user_prod'
GO

-- Create an environment variable AIRBNB_ENV with value development in computer and production in server
