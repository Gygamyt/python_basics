from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class DriverFactory:
    def __init__(self, browser: str = 'chrome', options: str = '_'):
        self.browser = browser.lower()
        self.options = options.lower()
        self.driver = None

    def shutDownBrowser(self):
        self.driver.quit()

    def getDriver(self):
        match self.browser:
            case 'chrome':
                self.driver = webdriver.Chrome(service=ChromeService())
            case 'firefox':
                self.driver = webdriver.Firefox()
            case _:
                raise Exception('Unsupported browser')
        return self.driver
