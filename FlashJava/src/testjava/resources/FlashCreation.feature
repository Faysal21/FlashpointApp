Feature: Flashpoint Allows Users To Create Flashcards

  Scenario: Flashcard Creation Works
    Given The User is on the login page
    When The User enters flash_user into the username input
    When The User enters pwd1 into the password input
    When The User clicks on the login button
    When The User is on the home page
    When The User clicks on the option to create a new deck
    When The User types 52 into the id input
    When The User enters basketball into the deck name input
    When The User clicks the submit deck button
    When The User enters who was the 2022 NBA MVP into the question input
    When The User enters Nikola Jokic into the answer input
    When The User clicks the submit card button
    Then The creation message should be Card successfully added to the deck
