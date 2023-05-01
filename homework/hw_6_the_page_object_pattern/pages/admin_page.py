from urllib.parse import urljoin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AdminPage:
    def __init__(self, driver):
        self._driver = driver
        self._url = urljoin(driver.browser_base_url, '/administration/')

    def open_products_page(self):
        self._driver.get(
            urljoin(self._url, 'index.php?route=catalog/product')
        )

    def is_element_present(self, element: tuple) -> bool:
        try:
            WebDriverWait(self._driver, 2).until(EC.presence_of_element_located(element))
            return True
        except TimeoutException:
            return False
