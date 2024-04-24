from selenium.webdriver.common.by import By
from data import ScooterData


class MainPageLocators:

    header = [By.XPATH, ".//div[contains(@class, 'Home_Header')]"]
    cookie_button = [By.XPATH, ".//button[text()='да все привыкли']"]
    scooter_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]"]
    yandex_logo = [By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]"]
    question_1 = [By.XPATH,
                  f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_1}']/../div"]
    answer_1 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_1}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_2 = [By.XPATH,
                  f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_2}']/../div"]
    answer_2 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_2}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_3 = [By.XPATH,
                  f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_3}']/../div"]
    answer_3 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_3}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_4 = [By.XPATH,
                  f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_4}']/../div"]
    answer_4 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_4}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_5 = [By.XPATH,
                  f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_5}']/../div"]
    answer_5 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_5}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_6 = [By.XPATH,
                  f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_6}']/../div"]
    answer_6 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_6}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_7 = [By.XPATH,
                  f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_7}']/../div"]
    answer_7 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_7}']"
                f"/..//../div[@class='accordion__panel']/p"]
    question_8 = [By.XPATH,
                  f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_8}']/../div"]
    answer_8 = [By.XPATH,
                f".//div[@class='accordion__button' and text()='{ScooterData.QUESTION_TEXT_8}']"
                f"/..//../div[@class='accordion__panel']/p"]
