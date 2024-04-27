from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def open_page(self, url):
        self.driver.get(url)


    def confirm_cookies(self, locator):
        self.wait_element(locator)
        self.click_element(locator)


    def scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def click_element(self, locator):
        self.driver.find_element(*locator).click()


    def text_element(self, locator):
        return self.driver.find_element(*locator).text


    def wait_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))


    def wait_page(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))


    def get_url(self):
        return self.driver.current_url


    def open_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])


    def set_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)
