CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	username VARCHAR,
	pwd VARCHAR,
	role VARCHAR
);

CREATE TABLE cards(
	id SERIAL PRIMARY KEY,
	question VARCHAR,
	answer VARCHAR,
	set_id NUMERIC
);

CREATE TABLE owners(
	owner_id NUMERIC,
	set_id NUMERIC
);