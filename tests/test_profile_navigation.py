from locators.stellar_locators import StellarLocators as SL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.helpers import login
from urls import BASE_URL, PROFILE_URL, LOGIN_URL

class TestProfileNavigation:

    def test_logout_from_profile(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()
        login(driver)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SL.PERSONAL_ACCOUNT_BUTTON)).click()
        logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SL.LOGOUT_BUTTON))
        logout_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL
