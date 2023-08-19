from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.locators import Locator


class DriverHelpers:
    DEFAULT_TIMEOUT = 20
    POLL_FREQUENCY = 0.5

    def custom_find_element(
            self,
            locator: 'Locator',
            timeout: int | float = DEFAULT_TIMEOUT,
            poll_frequency: int | float = POLL_FREQUENCY
    ):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
        return wait.until(EC.presence_of_element_located(locator))

    def element_is_exist(
            self,
            locator: 'Locator',
            timeout: int = DEFAULT_TIMEOUT,
            retry_count: int = 2
    ) -> bool:
        for count in range(retry_count):
            try:
                self.custom_find_element(locator, timeout)
                return True
            except WebDriverException as error:
                if isinstance(error, TimeoutException):
                    return False
                if count == retry_count - 1:
                    raise error
        return False
