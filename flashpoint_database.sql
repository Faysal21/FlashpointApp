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
	deck_id NUMERIC
);

CREATE TABLE decks(
	owner_id NUMERIC,
	deck_id NUMERIC,
	deck_name VARCHAR
);