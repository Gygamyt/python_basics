from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class HeaderPanel(BasePage):
    __magnifying_glass_element = (By.ID, 'magnifying-glass')
    __search_panel_element = (By.ID, 'search')
    __find_element = (By.CSS_SELECTOR, 'input[type="submit"][name="sa"][value="Найти"]')

    def __init__(self, driver):
        super().__init__(driver)

    def clickOnSearchAndEnterTheText(self, text: str):
        self.clickElementByLocator(self.__magnifying_glass_element)
        self.inputTextToElement(self.__search_panel_element, text)
        self.clickElementByLocator(self.__find_element)
        return self
