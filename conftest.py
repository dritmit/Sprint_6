import pytest
from selenium import webdriver
from settings import Settings


@pytest.fixture(scope='function')
def driver():
    fox_driver = webdriver.Firefox()
    fox_driver.maximize_window()
    fox_driver.get(Settings.MAIN_URL)
    yield fox_driver
    fox_driver.quit()
