import pytest
import allure
from conftest import driver
from page_objects.main_page import MainPage
from data import ScooterData
from locators.main_page_locators import MainPageLocators


class TestScooterRedirect:

    @allure.title('Проверка перехода на главную через логотип Самокат')
    @allure.description('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_main_page_redirect(self, driver):
        some_page = MainPage(driver)
        some_page.open_page(ScooterData.ORDER_URL)
        some_page.wait_element(MainPageLocators.scooter_logo)
        some_page.click_element(MainPageLocators.scooter_logo)
        some_page.wait_element(MainPageLocators.scooter_logo)
        redirect_url = some_page.get_url()

        assert redirect_url == ScooterData.MAIN_URL

    @allure.title('Проверка перехода на Дзен через логотип Яндекс')
    @allure.description('Если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_yandex_redirect(self, driver):
        some_page = MainPage(driver)
        some_page.open_page(ScooterData.ORDER_URL)
        some_page.wait_element(MainPageLocators.yandex_logo)
        some_page.click_element(MainPageLocators.yandex_logo)
        some_page.open_tab(1)
        some_page.wait_page(ScooterData.DZEN_URL)
        redirect_url = some_page.get_url()

        assert redirect_url == ScooterData.DZEN_URL
