from selenium import webdriver


class DriverFactory:
    def __init__(self, browser='chrome'):
        if browser.lower() == 'chrome':
            self.browser = webdriver.Chrome()

        elif browser.lower() == 'firefox':
            self.browser = webdriver.Firefox()

        else:
            raise ValueError('Browser must be either "chrome" or "firefox"')

    def open(self, url):
        self.browser.get(url)

    def shutDownBrowser(self):
        self.browser.quit()

    def getDriver(self):
        return self.browser
