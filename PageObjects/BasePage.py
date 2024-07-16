from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(driver, self.timeout)

    def open(self, url):
        self.driver.get(url)
        return self

    def findElement(self, locator):
        return (WebDriverWait(self.driver, self.timeout)
                .until(expected_conditions.presence_of_element_located(locator)))

    def clickElement(self, locator):
        element = self.findElement(locator)
        element.click()
        return self
