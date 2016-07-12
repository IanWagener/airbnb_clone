CREATE USER 'airbnb_user_prod'@'localhost' IDENTIFIED BY 'Us3r_Pr0d';

CREATE USER 'airbnb_user_dev'@'%' IDENTIFIED BY 'uS3r_d3\/';

CREATE DATABASE airbnb_dev CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE DATABASE	airbnb_prod CHARACTER SET utf8 COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON database.airbnb_dev TO 'airbnb_user_dev'@'%' IDENTIFIED BY 'uS3r_d3\/';

GRANT ALL PRIVILEGES ON	database.airbnb_prod TO 'airbnb_user_prod'@'localhost' IDENTIFIED BY 'Us3r_Pr0d';
