from locators.stellar_locators import StellarLocators as SL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.helpers import login
from urls import BASE_URL, PROFILE_URL

class TestHeaderNavigation:

    def test_click_logo_redirects_to_home(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()
        login(driver)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SL.LOGO_BUTTON)).click()
        WebDriverWait(driver, 10).until(lambda d: d.current_url == BASE_URL)
        assert driver.current_url == BASE_URL

    def test_click_constructor_redirects_to_home(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()
        login(driver)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SL.CONSTRUCTOR_BUTTON)).click()
        WebDriverWait(driver, 10).until(lambda d: d.current_url == BASE_URL)
        assert driver.current_url == BASE_URL
