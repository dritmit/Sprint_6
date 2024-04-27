import allure
from page_objects.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Скроллим до вопроса, кликаем и ждем появления ответа')
    def check_correct_answer_when_click_on_question(self, question_locator, answer_locator):

        self.scroll_page(question_locator)
        self.wait_element(question_locator)
        self.click_element(question_locator)
        self.wait_element(answer_locator)


    @allure.step('Ожидаем загрузки элемента содержащего гиперссылку, кликаем по нему, вновь ожидаем загрузки элемента')
    def main_page_redirect(self, main_page_link):
        self.wait_element(main_page_link)
        self.click_element(main_page_link)
        self.wait_element(main_page_link)


    @allure.step('Ожидаем загрузки элемента содержащего гиперссылку, кликаем по нему, переключаемся на новую вкладку, '
                 'ожидаем значение в адресной строке')
    def external_redirect(self, ext_link, url):
        self.wait_element(ext_link)
        self.click_element(ext_link)
        self.open_tab(1)
        self.wait_page(url)
