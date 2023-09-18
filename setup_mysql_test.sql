-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user on the specified databases
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
