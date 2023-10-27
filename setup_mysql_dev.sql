-- SQL Script to set up dev and test databases for AirBnB V2
CREATE DATABASE if NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
