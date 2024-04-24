import allure
import allure_pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.main_page import MainPage


class OrderPage(MainPage):

    #@allure.step('Вводим данные {value} в поле {locator}')
    def set_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def fill_in_for_whom_form(self, name_field, name,
                              surname_field, surname,
                              address_field, address,
                              metro_list, metro_station,
                              phone_field, phone):
        self.wait_element(name_field)
        self.set_value(name_field, name)
        self.set_value(surname_field, surname)
        self.set_value(address_field, address)
        self.click_element(metro_list)
        self.scroll_page(metro_station)
        self.click_element(metro_station)
        self.set_value(phone_field, phone)

    def fill_in_about_rent_form(self, rent_date, day_rent_date,
                                term_of_rent_list, term_of_rent_value,
                                color_checkbox,
                                comment_field, comment):
        self.wait_element(comment_field)
        self.click_element(rent_date)
        self.click_element(day_rent_date)
        self.click_element(term_of_rent_list)
        self.click_element(term_of_rent_value)
        self.click_element(color_checkbox)
        self.set_value(comment_field, comment)



