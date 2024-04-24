import allure
import allure_pytest
import pytest
from selenium import webdriver
from data import ScooterData


@pytest.fixture(scope='function')
#@allure.step('fixture')
def driver():
    fox_driver = webdriver.Firefox()
    fox_driver.maximize_window()
    fox_driver.get(ScooterData.MAIN_URL)

    yield fox_driver

    fox_driver.quit()
