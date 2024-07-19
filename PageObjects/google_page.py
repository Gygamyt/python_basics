from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class GooglePage(BasePage):
    search_bar_element = (By.ID, 'APjFqb')

    def __init__(self, driver):
        super().__init__(driver)
        self.open('https://www.google.com/')

    def click_search_bar_and_fill_with_request(self):
        self.clickElementByLocator(self.search_bar_element)
        self.inputTextToElement(self.search_bar_element, 'asdasdasd')

