import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from .locators import AdminPageLocators


class AdminPage:
    def __init__(self, driver, url):
        self._driver = driver
        self._url = url

    def open_products_page(self) -> None:
        self._driver.get(self._driver.current_url.replace('common/dashboard', 'catalog/product'))

    def delete_upper_product(self) -> str:
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.UPPER_PRODUCT_CHECKBOX)
        ).click()
        deleted_product_title = WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.UPPER_PRODUCT_TITLE)
        ).text
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.DELETE_BUTTON)
        ).click()
        Alert(self._driver).accept()
        time.sleep(1)  # Waiting for products to be updated in the table after deleting the top one

        return deleted_product_title

    @property
    def upper_product_title(self):
        return WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.UPPER_PRODUCT_TITLE)
        ).text
