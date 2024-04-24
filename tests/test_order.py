import pytest
import allure
from conftest import driver
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from data import ScooterData
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators


class TestScooterOrder:

    @allure.title('Заказ самоката через верхнюю кнопку Заказать')
    @allure.description('Точка входа - кнопка "Заказать" вверху страницы.'
                        ' Заполняем поля форм заказа валидными данными и проверяем'
                        'отображение подтверждения оформления заказа')
    def test_order_top(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(ScooterData.MAIN_URL)
        order_page.wait_element(OrderPageLocators.top_order_button)
        order_page.click_element(MainPageLocators.cookie_button)
        order_page.click_element(OrderPageLocators.top_order_button)
        order_page.fill_in_for_whom_form(OrderPageLocators.name_field, ScooterData.NAME_1,
                                         OrderPageLocators.surname_field, ScooterData.SURNAME_1,
                                         OrderPageLocators.address_field, ScooterData.ADDRESS_1,
                                         OrderPageLocators.metro_list, OrderPageLocators.metro_station,
                                         OrderPageLocators.phone_field, ScooterData.PHONE_1)
        order_page.click_element(OrderPageLocators.next_button)
        order_page.fill_in_about_rent_form(OrderPageLocators.rent_date, OrderPageLocators.day_rent_date,
                                           OrderPageLocators.term_of_rent_list, OrderPageLocators.term_of_rent_value,
                                           OrderPageLocators.color_checkbox,
                                           OrderPageLocators.comment_field, ScooterData.COMMENT_1)
        order_page.click_element(OrderPageLocators.form_order_button)
        order_page.wait_element(OrderPageLocators.want_to_order_header)
        order_page.click_element(OrderPageLocators.yes_button)
        order_page.wait_element(OrderPageLocators.order_placed_header)

        order_info = order_page.text_element(OrderPageLocators.order_info)

        assert 'Номер заказа' in order_info

    @allure.title('Заказ самоката через нижнюю кнопку Заказать')
    @allure.description('Точка входа - кнопка "Заказать" внизу страницы.'
                        ' Заполняем поля форм заказа валидными данными и проверяем'
                        'отображение подтверждения оформления заказа')
    def test_order_bottom(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(ScooterData.MAIN_URL)
        order_page.wait_element(OrderPageLocators.top_order_button)
        order_page.click_element(MainPageLocators.cookie_button)
        order_page.scroll_page(OrderPageLocators.bottom_order_button)
        order_page.click_element(OrderPageLocators.bottom_order_button)
        order_page.fill_in_for_whom_form(OrderPageLocators.name_field, ScooterData.NAME_2,
                                         OrderPageLocators.surname_field, ScooterData.SURNAME_2,
                                         OrderPageLocators.address_field, ScooterData.ADDRESS_2,
                                         OrderPageLocators.metro_list, OrderPageLocators.metro_station,
                                         OrderPageLocators.phone_field, ScooterData.PHONE_2)
        order_page.click_element(OrderPageLocators.next_button)
        order_page.fill_in_about_rent_form(OrderPageLocators.rent_date, OrderPageLocators.day_rent_date,
                                           OrderPageLocators.term_of_rent_list, OrderPageLocators.term_of_rent_value,
                                           OrderPageLocators.color_checkbox,
                                           OrderPageLocators.comment_field, ScooterData.COMMENT_2)
        order_page.click_element(OrderPageLocators.form_order_button)
        order_page.wait_element(OrderPageLocators.want_to_order_header)
        order_page.click_element(OrderPageLocators.yes_button)
        order_page.wait_element(OrderPageLocators.order_placed_header)

        order_info = order_page.text_element(OrderPageLocators.order_info)

        assert 'Номер заказа' in order_info
