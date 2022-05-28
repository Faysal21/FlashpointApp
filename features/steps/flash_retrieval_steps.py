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


@when('When The User clicks on a set they want to study')
def press_deck_link(context):
    flash_home: FlashHomePage = context.flash_home
    flash_home.deck_link().click()


@then('Then The deck name should be {deckname}')
def verify_deck_name(context, deckname):
    test: unittest.TestCase = context.unittest
    test.assertEquals(context.driver.deckname, deckname)
