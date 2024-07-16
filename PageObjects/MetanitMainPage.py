from selenium.webdriver.common.by import By

import BasePage


class MetanitMainPage(BasePage):
    metanitElement = (By.CLASS_NAME, 'logoTitle')

    def __init__(self, driver):
        super().__init__(driver)
