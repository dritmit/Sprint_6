import pytest
import allure
import allure_pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage:

    #@allure.step('инициализация')
    def __init__(self, driver):
        self.driver = driver

    #@allure.step('Открываем страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    #@allure.step('Скроллим страницу до элемента {locator}')
    def scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    #@allure.step('Клик по элементу {locator}')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    #@allure.step('Получаем текст элемента {locator}')
    def text_element(self, locator):
        return self.driver.find_element(*locator).text

    #@allure.step('Ожидание загрузки элемента {locator}')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

   # @allure.step('Ожидание загрузки страницы {url}')
    def wait_page(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    #@allure.step('Получаем текущую страницу {url}')
    def get_url(self):
        return self.driver.current_url

    #@allure.step('Переходим на вкладку с номером {tab_number}')
    def open_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    #@allure.step('Скроллим до элемента, ждем появления и кликаем {locator}')
    def scroll_wait_click_element(self, locator):
        self.scroll_page(locator)
        self.wait_element(locator)
        self.click_element(locator)
