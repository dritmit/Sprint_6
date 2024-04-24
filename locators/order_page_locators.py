from selenium.webdriver.common.by import By
from data import ScooterData


class OrderPageLocators:

    top_order_button = [By.XPATH, ".//div[contains(@class, 'Header')]/button[text()='Заказать']"]
    bottom_order_button = [By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"]

    name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_list = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    metro_station = [By.XPATH, ".//div[text()='Нижегородская']"]
    phone_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]

    next_button = [By.XPATH, ".//div[contains(@class, 'Order_NextButton')]/button[text()='Далее']"]

    rent_date = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    day_rent_date = [By.XPATH, ".//div[contains(@class, 'react-datepicker__day') and text()='27']"]
    term_of_rent_list = [By.XPATH, ".//div[text()='* Срок аренды']"]
    term_of_rent_value = [By.XPATH, ".//div[text()='двое суток']"]
    color_checkbox = [By.XPATH, ".//label[text()='чёрный жемчуг']"]
    comment_field = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]

    form_order_button = [By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"]
    want_to_order_header = [By.XPATH, ".//div[text()='Хотите оформить заказ?']"]
    yes_button = [By.XPATH, ".//button[text()='Да']"]

    order_placed_header = [By.XPATH, ".//div[text()='Заказ оформлен']"]
    order_info = [By.XPATH, ".//div[contains(@class, 'Order_Text')]"]
