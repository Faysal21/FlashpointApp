CREATE TABLE users(
	id NUMERIC PRIMARY KEY,
	username VARCHAR,
	pwd VARCHAR
);

CREATE TABLE cards(
	id NUMERIC PRIMARY KEY,
	owner_id NUMERIC,
	question VARCHAR,
	answer VARCHAR
);