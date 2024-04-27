import pytest
import allure
from conftest import driver
from page_objects.order_page import OrderPage
from settings import Settings
from data import Data
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators


class TestScooterOrder:

    @allure.title('Заказ самоката. Две точки входа: кнопки Заказать вверху и внизу главной страницы')
    @allure.description('Кликаем кнопку "Заказать". Заполняем поля форм заказа валидными данными и проверяем'
                        'отображение подтверждения оформления заказа')
    @pytest.mark.parametrize("order_button, name, surname, address, phone, comment",
                             [(BasePageLocators.top_order_button, Data.NAME_1, Data.SURNAME_1, Data.ADDRESS_1,
                               Data.PHONE_1, Data.COMMENT_1),
                              (BasePageLocators.bottom_order_button, Data.NAME_2, Data.SURNAME_2, Data.ADDRESS_2,
                               Data.PHONE_2, Data.COMMENT_2)])
    def test_order_top(self, driver, order_button, name, surname, address, phone, comment):
        order_page = OrderPage(driver)
        order_page.open_page(Settings.MAIN_URL)
        order_page.confirm_cookies(BasePageLocators.cookie_button)
        order_page.click_order_button(order_button)
        order_page.fill_in_for_whom_form(OrderPageLocators.name_field, name,
                                         OrderPageLocators.surname_field, surname,
                                         OrderPageLocators.address_field, address,
                                         OrderPageLocators.metro_list, OrderPageLocators.metro_station,
                                         OrderPageLocators.phone_field, phone,
                                         OrderPageLocators.next_button)
        order_page.fill_in_about_rent_form(OrderPageLocators.rent_date, OrderPageLocators.day_rent_date,
                                           OrderPageLocators.term_of_rent_list, OrderPageLocators.term_of_rent_value,
                                           OrderPageLocators.color_checkbox,
                                           OrderPageLocators.comment_field, comment,
                                           OrderPageLocators.form_order_button)
        order_page.confirm_order(OrderPageLocators.want_to_order_header, OrderPageLocators.yes_button,
                                 OrderPageLocators.order_placed_header)
        order_info = order_page.text_element(OrderPageLocators.order_info)
        assert 'Номер заказа' in order_info
