CREATE TABLE users(
	id NUMERIC PRIMARY KEY,
	username VARCHAR,
	pwd VARCHAR
);

CREATE TABLE cards(
	id NUMERIC PRIMARY KEY,
	owner_id NUMERIC,
	deck_id NUMERIC,
	deck_order NUMERIC,
	question VARCHAR,
	answer VARCHAR
);