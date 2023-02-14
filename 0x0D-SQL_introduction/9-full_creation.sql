-- creates a table second_table in the database hbtn_0c_0 in your MySQL server
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- add multiples rows
INSERT INTO second_table (id, name, score) VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "BOB", 14),
	(4, "George", 8);
