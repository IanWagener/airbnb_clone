CREATE USER 'airbnb_user_prod'@'localhost' IDENTIFIED BY '';

CREATE USER 'airbnb_user_dev'@'%' IDENTIFIED BY '';

CREATE DATABASE airbnb_dev CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE DATABASE	airbnb_prod CHARACTER SET utf8 COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON database.airbnb_dev TO 'airbnb_user_dev'@'%' IDENTIFIED BY '';

GRANT ALL PRIVILEGES ON	database.airbnb_prod TO 'airbnb_user_prod'@'localhost' IDENTIFIED BY '';
