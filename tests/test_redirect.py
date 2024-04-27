import allure
from conftest import driver
from page_objects.main_page import MainPage
from settings import Settings
from locators.base_page_locators import BasePageLocators


class TestScooterRedirect:

    @allure.title('Проверка перехода на главную через логотип Самокат')
    @allure.description('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_main_page_redirect_scooter_logo(self, driver):
        some_page = MainPage(driver)
        some_page.open_page(Settings.ORDER_URL)
        some_page.main_page_redirect(BasePageLocators.scooter_logo)
        assert some_page.get_url() == Settings.MAIN_URL


    @allure.title('Проверка перехода на Дзен через логотип Яндекс')
    @allure.description('Если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_external_redirect_yandex_logo(self, driver):
        some_page = MainPage(driver)
        some_page.open_page(Settings.ORDER_URL)
        some_page.external_redirect(BasePageLocators.yandex_logo, Settings.DZEN_URL)
        assert some_page.get_url() == Settings.DZEN_URL
