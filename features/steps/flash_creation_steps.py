# import unittest
#
# from behave import when, then
#
# from features.pages.flash_home import FlashHomePage
#
#
# @when('When The User clicks on the option to create a new deck')
# def press_create_new_set(context):
#     flash_home: FlashHomePage = context.flash_home
#     flash_home.create_btn().click()
#
#
# @when('When The User types 50 in the id input')
# def click_submit_btn(context):
#     flash_home: FlashHomePage = context.flash_home
#     flash_home.deck_id_input().send_keys("50")
#
#
# @when('When The answer should be {answer}')
# def verify_answer(context, answer):
#     test: unittest.TestCase = context.unittest
#     test.assertEquals(context.driver.answer, answer)
#
#
# @when('When The User clicks the next card button')
# def press_next_button(context):
#     flash_home: FlashHomePage = context.flash_home
#     flash_home.next_btn().click()
#
#
# @then('Then The next question should be {question} or the set should be finished')
# def verify_next_question(context, question):
#     test: unittest.TestCase = context.unittest
#     test.assertEquals(context.driver.question, question)
#
#
#
#
#     When The User enters a <deckname> in the deck name input
#     When The User clicks the submit deck button
#     When The User enters a <question> into the question input
#     When The User enters an <answer> into the answer input
#     When The User clicks the submit card button
#     Then The creation message should be <message>