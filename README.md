# FlashpointApp
An online flashcard application that allows users to study by submitting answers to questions. The users will then be given feedback. Additionally, designated card makers can create flash cards for other users to study with.
## Technologies Used
- Python (Version 3.10)
- Java 8
- PostgresSQL
- Javascript, HTML, CSS
- Selenium
## Features 
- Users can answer questions given on flashcards
- Depending on a user's answer, they are given feedback on its correctness
- User with creation roles can create a deck of flashcards as well as individual flashcards
## Getting Started
- Ensure Python 3 is installed
- Ensure Java 8 is installed
- Clone this repo "git clone https://github.com/Faysal21/FlashpointApp.git"
- For Java: Ensure you have Javalin imported in your dependecies
- For Java: Ensure you connect to your database in AWS RDS using JDBC
- For Python: Set up a database connection with your AWS RDS
- For Python: Install Flask, Flask-cors, and Psycopg2
- Run application in either Java or Python and open login-register.html in a web browser
## Usage
Register a new account or log in with existing credentials. If you are a standard user, then select flashcards that are available and answer their questions. If you are a flashcard maker and want to create flashcards, use the tools on the web page to create a new deck and then create individual flashcards until you are satisfied with the amount of cards.
