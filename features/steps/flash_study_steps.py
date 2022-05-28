import unittest

from behave import when, then

from features.pages.flash_home import FlashHomePage


@when('When The User types an answer')
def types_into_answer_input(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.answer_input().send_keys("answer")


@when('When The User clicks the submit button')
def click_submit_btn(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.submit_btn().click()


@when('When The answer should be {answer}')
def verify_answer(context, answer):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.answer, answer)


@when('When The User clicks the next card button')
def press_next_button(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.next_btn().click()


@then('Then The next question should be {question} or the set should be finished')
def verify_next_question(context, question):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.question, question)
