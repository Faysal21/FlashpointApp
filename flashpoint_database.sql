CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	username VARCHAR,
	pwd VARCHAR,
	user_role VARCHAR
);

INSERT INTO users values(default, 'flash_user', 'pwd1', 'admin'),

CREATE TABLE decks(
	deck_id NUMERIC PRIMARY KEY,
	deck_name VARCHAR,
	user_id FOREIGN KEY
);

INSERT INTO decks values(1, 'Football Terminology', 1)

CREATE TABLE cards(
	card_id int PRIMARY KEY,
	question VARCHAR,
	answer VARCHAR,
	deck_id NUMERIC FOREIGN KEY
);

INSERT INTO cards values(1, 'Who won the first Super Bowl in history?', 'Green Bay Packers', 1),
INSERT INTO cards values(2, 'How many players are on each team in American football?', 11, 1),
INSERT INTO cards values(3, 'What are the dimensions of an American football field?', '120 yards long and 53.3 yards wide', 1)
