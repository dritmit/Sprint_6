import pytest
import allure
from page_objects.main_page import MainPage
from settings import Settings
from text_on_page import TextOnPage
from locators.main_page_locators import MainPageLocators


class TestScooterFaq:

    @allure.title('Выпадающий список в разделе "Вопросы о важном"')
    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @pytest.mark.parametrize("question_text, answer_text, true_answer",
                             [(MainPageLocators.question_1, MainPageLocators.answer_1, TextOnPage.ANSWER_1),
                              (MainPageLocators.question_2, MainPageLocators.answer_2, TextOnPage.ANSWER_2),
                              (MainPageLocators.question_3, MainPageLocators.answer_3, TextOnPage.ANSWER_3),
                              (MainPageLocators.question_4, MainPageLocators.answer_4, TextOnPage.ANSWER_4),
                              (MainPageLocators.question_5, MainPageLocators.answer_5, TextOnPage.ANSWER_5),
                              (MainPageLocators.question_6, MainPageLocators.answer_6, TextOnPage.ANSWER_6),
                              (MainPageLocators.question_7, MainPageLocators.answer_7, TextOnPage.ANSWER_7),
                              (MainPageLocators.question_8, MainPageLocators.answer_8, TextOnPage.ANSWER_8)])
    def test_faq_open_question(self, driver, question_text, answer_text, true_answer):
        main_page = MainPage(driver)
        main_page.open_page(Settings.MAIN_URL)
        main_page.check_correct_answer_when_click_on_question(question_text, answer_text)
        answer_on_page = main_page.text_element(answer_text)
        assert answer_on_page == true_answer
