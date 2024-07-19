from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.__driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.__driver, self.timeout)

    def open(self, url):
        self.__driver.get(url)
        return self

    def findElement(self, locator):
        return (WebDriverWait(self.__driver, self.timeout)
                .until(expected_conditions.presence_of_element_located(locator)))

    def clickElementByLocator(self, locator):
        element = self.findElement(locator)
        element.click()
        return self

    def inputTextToElement(self, locator, text):
        element = self.findElement(locator)
        element.click()
        WebDriverWait(element, 5).until(expected_conditions.element_to_be_clickable(element))
        element.send_keys(text)
        return self
