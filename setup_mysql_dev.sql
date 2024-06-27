-- Prepares a server 'hbnb_dev_db' for the AirBnB Project

-- Creates the DATABASE if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates the USER if it doesn't exist and grant all privileges on
-- 'hbnb_dev_db' database to the new USER
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Also grant the SELECT privilege on performance_scheme to the new USER
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
