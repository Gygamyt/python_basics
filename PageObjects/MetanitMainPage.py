from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class MetanitMainPage(BasePage):
    __metanitElement = (By.CLASS_NAME, 'logoTitle')

    def __init__(self, driver):
        super().__init__(driver)
        self.__base_url = 'https://metanit.com/'

    def clickMetanitElement(self):
        self.clickElementByLocator(self.__metanitElement)
        return self

    def openMetanitPage(self):
        self.open(self.__base_url)
