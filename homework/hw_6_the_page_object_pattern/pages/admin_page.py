import pytest
from urllib.parse import urljoin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AdminPage:
    def __init__(self, driver, user_token):
        self._driver = driver
        self._url = urljoin(driver.browser_base_url, '/administration/')
        self.user_token = user_token

    def open_products_page(self):
        self._driver.get(
            urljoin(self._url, f'index.php?route=catalog/product&user_token={self.user_token}')
        )

    def is_element_present(self, element: tuple) -> bool:
        try:
            WebDriverWait(self._driver, 2).until(EC.presence_of_element_located(element))
            return True
        except TimeoutException:
            return False
