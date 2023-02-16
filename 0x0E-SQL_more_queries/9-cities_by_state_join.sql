-- lists all cities contained in the database hbtn_0d_usa
SELECT id, name, name FROM states
INNER JOIN cities
ON states.id=cities.state_id
SORT BY cities.id ASC;
