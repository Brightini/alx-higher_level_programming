-- This script lists all cities contained in a database
-- It displays each record in the format cities.id cities.name states.name

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states on cities.state_id = states.id
ORDER BY id;
