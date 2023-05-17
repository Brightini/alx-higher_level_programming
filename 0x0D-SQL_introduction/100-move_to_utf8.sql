-- This script converts hbtn_0c_0 database to UTF8

-- Select database
USE hbtn_0c_0;

-- Convert database to utf8mb4 character set
ALTER DATABASE hbtn_0c_0
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;

-- Convert each table in database to utf
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert field in first_table table to UTF
ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
