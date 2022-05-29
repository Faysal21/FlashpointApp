import unittest

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.flash_home import FlashHomePage


@given('The User is on the home page')
def get_to_flash_home(context):
    driver: WebDriver = context.driver
    driver.get(
        'file:///C:/Users/patri/Documents/Coding/RevTraining/Python/Flashpoint/FlashpointApp/flashpoint-test.html'
    )


@when('The User clicks on the movie directors link')
def press_deck_link(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.deck_link().click()


@when('The deck name should be movie directors')
def verify_deck_name(context):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.title, "Movie Directors")


@when('The User types an answer')
def types_into_answer_input(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.answer_input().send_keys("answer")


@when('The User clicks the submit button')
def click_submit_btn(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.submit_btn().click()


@when('The answer should be Russo Brothers')
def verify_answer(context):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.answer_display(), "Russo Brothers")


@when('The User clicks the next card button')
def press_next_button(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.next_btn().click()


@then('The next question should be Who directed Independence Day?')
def verify_next_question(context):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.next_question_display(), 'Who directed Independence Day?')
