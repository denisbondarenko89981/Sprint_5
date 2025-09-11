import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.stellar_locators import StellarLocators as SL
from helpers.helpers import wait_for_tab
from urls import BASE_URL


class TestConstructorTabs:
    @pytest.mark.parametrize("locator, name, prep_locator", [
        (SL.SAUCES_TAB, "Соусы", SL.FILLINGS_TAB),     # сначала на "Начинки", потом в "Соусы"
        (SL.FILLINGS_TAB, "Начинки", SL.SAUCES_TAB),   # сначала на "Соусы", потом в "Начинки"
        (SL.BUNS_TAB, "Булки", SL.SAUCES_TAB),         # сначала на "Соусы", потом в "Булки"
    ])
    def test_switch_tabs(self, driver, locator, name, prep_locator):
        driver.get(BASE_URL)

        # подготовительный клик
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(prep_locator)).click()
        wait_for_tab(driver, driver.find_element(*prep_locator).text)

        # основной клик
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locator)).click()
        active_tab = wait_for_tab(driver, name)

        assert active_tab.text == name, (f"Ожидали, что активная вкладка будет '{name}', а получили '{active_tab.text}'")

