Feature: Flashpoint Allows Users To Study With Flashcards

  Scenario: Flashcard Works
    Given The User is on the home page
    When The User clicks on a set they want to study
    When The User types an answer
    When The User clicks the submit button
    When The answer is revealed
    When The User clicks the 'next card' button
    Then The next question should display or the set should be finished
