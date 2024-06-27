-- Prepare a MySQL server

-- Creates a database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a new USER if it doesn't exists and grants all privileges of hbnb_test_db
-- to it.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants the SELECT privilege of performance_scheme to the new user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
