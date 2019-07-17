-- Lists all cities in a database
-- Lists all cities in a database
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id
