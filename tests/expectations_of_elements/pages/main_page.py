from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver, url='https://www.opencart.com/'):
        self._driver = driver
        self._url = url

    def open(self) -> None:
        self._driver.get(self._url)

    def is_element_present(self, element) -> bool:
        try:
            WebDriverWait(self._driver, 1).until(EC.presence_of_element_located(element))
        except TimeoutException:
            return False
        return True
