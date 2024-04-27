from selenium.webdriver.common.by import By
from text_on_page import TextOnPage


class MainPageLocators:

    question_1 = [By.XPATH, f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_1}']/../div"]
    answer_1 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_1}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_2 = [By.XPATH, f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_2}']/../div"]
    answer_2 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_2}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_3 = [By.XPATH, f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_3}']/../div"]
    answer_3 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_3}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_4 = [By.XPATH, f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_4}']/../div"]
    answer_4 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_4}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_5 = [By.XPATH, f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_5}']/../div"]
    answer_5 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_5}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_6 = [By.XPATH, f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_6}']/../div"]
    answer_6 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_6}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_7 = [By.XPATH, f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_7}']/../div"]
    answer_7 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_7}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_8 = [By.XPATH, f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_8}']/../div"]
    answer_8 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{TextOnPage.QUESTION_8}']"
                f"/..//../div[@class='accordion__panel']/p"]