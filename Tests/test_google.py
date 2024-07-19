import time

from Fixtures.DriverFixtures import setup_driver
from PageObjects.google_page import GooglePage


def test_google(setup_driver):
    page = GooglePage(setup_driver)
    page.click_search_bar_and_fill_with_request()
    time.sleep(6)
