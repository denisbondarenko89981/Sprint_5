from locators.stellar_locators import StellarLocators as SL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers.helpers import login
from urls import BASE_URL

class TestLogin:

    def test_login_via_personal_account(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*SL.REGISTER_LINK).click()
        driver.find_element(*SL.LOGIN_LINK).click()
        login(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_login_via_recover_form(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*SL.RESTORE_LINK).click()
        driver.find_element(*SL.LINK_LOGIN).click()
        login(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_login_via_home_login_button(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SL.LOGIN_ACCOUNT).click()
        login(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_login_via_register_form(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*SL.REGISTER_LINK).click()
        driver.find_element(*SL.LOGIN_LINK).click()
        login(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL
