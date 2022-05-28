from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class FlashHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def deck_link(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/table/tbody/tr/tr[3]/td/a")

    def deck_name(self):
        return self.driver.find_element(by=By.ID, value="deckName")

    def answer_input(self):
        return self.driver.find_element(by=By.ID, value="cardAnswer")

    def submit_btn(self):
        return self.driver.find_element(by=By.ID, value="AnswerSubmit")

    def answer_display(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div/div[2]/h2/span")

    def next_btn(self):
        return self.driver.find_element(by=By.ID, value="nextQuestion")

    def next_question_display(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div/div[1]/h2/span")

