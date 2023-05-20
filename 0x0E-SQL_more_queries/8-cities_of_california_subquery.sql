-- This script lists all records in a table that can be found in another table

SELECT * FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY id;
