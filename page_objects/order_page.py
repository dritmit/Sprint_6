import allure

from page_objects.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Ждем появления кнопки и кликаем ее')
    def click_order_button(self, locator):
        self.wait_element(locator)
        self.click_element(locator)


    @allure.step('Заполняем данными поля форма "Для кого самокат"')
    def fill_in_for_whom_form(self, name_field, name,
                              surname_field, surname,
                              address_field, address,
                              metro_list, metro_station,
                              phone_field, phone, next_button):
        self.wait_element(name_field)
        self.set_value(name_field, name)
        self.set_value(surname_field, surname)
        self.set_value(address_field, address)
        self.click_element(metro_list)
        self.scroll_page(metro_station)
        self.click_element(metro_station)
        self.set_value(phone_field, phone)
        self.click_element(next_button)


    @allure.step('Заполняем данными поля форма "Про аренду"')
    def fill_in_about_rent_form(self, rent_date, day_rent_date,
                                term_of_rent_list, term_of_rent_value,
                                color_checkbox,
                                comment_field, comment, form_order_button):
        self.wait_element(comment_field)
        self.click_element(rent_date)
        self.click_element(day_rent_date)
        self.click_element(term_of_rent_list)
        self.click_element(term_of_rent_value)
        self.click_element(color_checkbox)
        self.set_value(comment_field, comment)
        self.click_element(form_order_button)


    @allure.step('Подтвердаем заказ после заполнения форм')
    def confirm_order(self, want_to_order_header, yes_button, confirmation):
        self.wait_element(want_to_order_header)
        self.click_element(yes_button)
        self.wait_element(confirmation)
