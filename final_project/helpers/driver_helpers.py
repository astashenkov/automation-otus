from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.support.wait import POLL_FREQUENCY

from helpers.locators import Locator


class DriverHelpers:
    DEFAULT_TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    def custom_find_element(self: 'WebDriver', locator: 'Locator', timeout: 'Digit' = DEFAULT_TIMEOUT) -> 'WebElement':
        with implicitly_wait_manager(self):
            return self.wait(timeout).until(
                method=lambda _driver: _driver.find_element(*locator),
                message=f'Could not find element by locator - {locator}'
            )

    def custom_find_elements(
            driver,
            locator: 'Locator',
            timeout: int = DEFAULT_TIMEOUT
    ) -> list:
        with implicitly_wait_manager(self, timeout):
            return self.find_elements(*locator)

    def element_is_exist(
            self,
            driver,
            locator: 'Locator',
            timeout: int = DEFAULT_TIMEOUT,
            retry_count: int = 2
    ) -> bool:
        for count in range(retry_count):
            try:
                driver.custom_find_element(locator, timeout)
                return True
            except WebDriverException as error:
                if isinstance(error, TimeoutException):
                    return False
                logging.warning('element_is_exist catch "%s" %s', type(error).__name__, error)
                if count == retry_count - 1:
                    raise error
        return False

    def wait(
            self: 'WebDriver',
            timeout: int | float = DEFAULT_TIMEOUT,
            poll_frequency: int | float = POLL_FREQUENCY,
            ignored_exceptions: list[Type[Exception]] | None = None
    ):
        return WebDriverWait(self, timeout, poll_frequency, ignored_exceptions)
