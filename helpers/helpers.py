from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.stellar_locators import StellarLocators as SL
from data.test_data import TEST_EMAIL, TEST_PASSWORD

def login(driver):
    driver.find_element(*SL.LOGIN_EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(*SL.LOGIN_PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(*SL.LOGIN_SUBMIT).click()

def wait_for_tab(driver, tab_text, timeout=10):
    return WebDriverWait(driver, timeout).until(
        lambda d: next(
            (el for el in d.find_elements(*SL.CONSTRUCTOR_TABS)
             if tab_text in el.text and 'tab_tab_type_current' in el.get_attribute("class")),
            False
        ),
        message=f"Вкладка '{tab_text}' не стала активной"
    )
