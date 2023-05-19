-- This script creates a MySQL server user

-- Create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Reload grant tables to ensure new privileges are put into effect
FLUSH PRIVILEGES;
