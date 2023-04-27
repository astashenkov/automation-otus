from .main_page import MainPage
from urllib.parse import urljoin


class LoginToAdminPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url = urljoin(driver.browser_base_url, '/administration')
