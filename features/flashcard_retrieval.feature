Feature: Flashpoint Allows Users To Study With Flashcards

  Scenario: Flashcard Retrieval Works
    Given The User is on the home page
    When The User clicks on the movie directors link
    When The User is on the movie directors set
    When The User types answer
    When The User clicks the submit button
    When The answer should be Russo Brothers
    When The User clicks the next card button
    Then The next question should be Who directed Independence Day?
