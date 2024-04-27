from selenium.webdriver.common.by import By


class BasePageLocators:

    header = [By.XPATH, ".//div[contains(@class, 'Home_Header')]"]
    cookie_button = [By.XPATH, ".//button[text()='да все привыкли']"]
    scooter_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"]
    yandex_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]"]
    top_order_button = [By.XPATH, ".//div[contains(@class, 'Header')]/button[text()='Заказать']"]
    bottom_order_button = [By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"]