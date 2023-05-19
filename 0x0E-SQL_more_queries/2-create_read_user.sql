-- This script creates a database and a user

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant user privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
