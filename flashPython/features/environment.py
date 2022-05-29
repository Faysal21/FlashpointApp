import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.flash_home import FlashHomePage


def before_all(context):
    driver: WebDriver = webdriver.Chrome(
        "C:/Users/patri/Documents/Coding/RevTraining/Python/chromedriver.exe")
    flash_home_page = FlashHomePage(driver)

    test = unittest.TestCase()

    context.driver = driver
    context.flash_home = flash_home_page
    context.unittest = test
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")


