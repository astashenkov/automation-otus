from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._url = driver.browser_base_url

    def open(self) -> None:
        self._driver.get(self._url)

    def is_element_present(self, element: tuple) -> bool:
        try:
            WebDriverWait(self._driver, 2).until(EC.presence_of_element_located(element))
        except TimeoutException:
            return False
        return True
