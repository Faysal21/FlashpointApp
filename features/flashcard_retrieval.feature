Feature: Flashpoint Allows Users To Select Flashcards To Study With

  Scenario: Flashcard Retrieval Works
    Given The User is on the home page
    When The User clicks on a set they want to study
    Then The deck name should be <deckname>

