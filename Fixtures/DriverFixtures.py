import pytest

from WebDriver.DriverFactory import DriverFactory


@pytest.fixture
def setup_driver():
    driver_factory = DriverFactory(browser='chrome')
    driver = driver_factory.getDriver()
    yield driver
    driver_factory.shutDownBrowser()