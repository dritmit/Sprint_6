import pytest
import allure
import allure_pytest
from conftest import driver
from page_objects.main_page import MainPage
from data import ScooterData
from locators.main_page_locators import MainPageLocators


class TestScooterFaq:

    @allure.title('Выпадающий список в разделе "Вопросы о важном"')
    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @pytest.mark.parametrize("question, answer, answer_text",
                             [(MainPageLocators.question_1, MainPageLocators.answer_1, ScooterData.ANSWER_TEXT_1),
                              (MainPageLocators.question_2, MainPageLocators.answer_2, ScooterData.ANSWER_TEXT_2),
                              (MainPageLocators.question_3, MainPageLocators.answer_3, ScooterData.ANSWER_TEXT_3),
                              (MainPageLocators.question_4, MainPageLocators.answer_4, ScooterData.ANSWER_TEXT_4),
                              (MainPageLocators.question_5, MainPageLocators.answer_5, ScooterData.ANSWER_TEXT_5),
                              (MainPageLocators.question_6, MainPageLocators.answer_6, ScooterData.ANSWER_TEXT_6),
                              (MainPageLocators.question_7, MainPageLocators.answer_7, ScooterData.ANSWER_TEXT_7),
                              (MainPageLocators.question_8, MainPageLocators.answer_8, ScooterData.ANSWER_TEXT_8)])
    def test_faq_open_question(self, driver, question, answer, answer_text):
        main_page = MainPage(driver)
        main_page.open_page(ScooterData.MAIN_URL)
        main_page.scroll_wait_click_element(question)
        main_page.wait_element(answer)

        assert main_page.text_element(answer) == answer_text
