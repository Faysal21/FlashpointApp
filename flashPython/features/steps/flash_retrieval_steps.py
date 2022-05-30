import unittest
from time import sleep

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from features.pages.flash_home import FlashHomePage


@given('The User is on the home page')
def get_to_flash_home(context):
    driver: WebDriver = context.driver
    driver.get(
        'file:///C:/Users/patri/Documents/Coding/RevTraining/Python/Flashpoint/FlashpointApp/flashFront/homepage.html'
    )
    sleep(1)


@when('The User clicks on the movie directors link')
def press_deck_link(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.deck_link().click()
    sleep(.5)


@when('The User is on the movie directors set')
def verify_deck_name(context):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.title, "Movie Directors")
    sleep(.5)


@when('The User types answer')
def types_into_answer_input(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.answer_input().send_keys("answer")
    sleep(.5)


@when('The User clicks the submit button')
def click_submit_btn(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.submit_btn().click()
    sleep(1)


@when('The answer should be Roland Emmerich')
def verify_answer(context):
    flash_home: FlashHomePage = context.flash_home
    test: unittest.TestCase = context.unittest
    test.assertEquals(flash_home.answer_display(), "Roland Emmerich")
    sleep(1)


@when('The User clicks the next card button')
def press_next_button(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.next_btn().click()
    sleep(.5)


@then('The next question should be Who directed Avengers Infinity War')
def verify_next_question(context):
    flash_home: FlashHomePage = context.flash_home
    test: unittest.TestCase = context.unittest
    test.assertEquals(flash_home.next_question_display(), 'Who directed Avengers Infinity War')
    sleep(1)
