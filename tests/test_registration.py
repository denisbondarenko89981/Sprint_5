from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators.stellar_locators import StellarLocators as SL
from urls import BASE_URL, LOGIN_URL, REGISTER_URL
from data.test_data import ERROR_SHORT_PASSWORD

class TestRegistration:

    def test_success_registration(self, driver, unique_user_data):
        driver.get(BASE_URL)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*SL.REGISTER_LINK).click()

        driver.find_element(*SL.REGISTER_NAME).send_keys(unique_user_data["name"])
        driver.find_element(*SL.REGISTER_EMAIL).send_keys(unique_user_data["email"])
        driver.find_element(*SL.REGISTER_PASSWORD).send_keys(unique_user_data["password"])
        driver.find_element(*SL.REGISTER_SUBMIT).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url == LOGIN_URL)
        assert driver.current_url == LOGIN_URL

    def test_registration_with_short_password(self, driver, unique_user_data):
        driver.get(BASE_URL)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*SL.REGISTER_LINK).click()

        driver.find_element(*SL.REGISTER_NAME).send_keys(unique_user_data["name"])
        driver.find_element(*SL.REGISTER_EMAIL).send_keys(unique_user_data["email"])
        driver.find_element(*SL.REGISTER_PASSWORD).send_keys("123")
        driver.find_element(*SL.REGISTER_SUBMIT).click()

        error_text = driver.find_element(*SL.REGISTER_ERROR).text
        assert ERROR_SHORT_PASSWORD in error_text
