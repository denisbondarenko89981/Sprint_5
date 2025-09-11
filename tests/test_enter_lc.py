from locators.stellar_locators import StellarLocators as SL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.helpers import login
from urls import BASE_URL, PROFILE_URL

class TestEnterPersonalAccount:

    def test_success_enter_lc(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*SL.PERSONAL_ACCOUNT_BUTTON).click()
        login(driver)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SL.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 10).until(lambda d: d.current_url == PROFILE_URL)
        assert driver.current_url == PROFILE_URL
