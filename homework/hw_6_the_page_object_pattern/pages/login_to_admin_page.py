from .admin_page import AdminPage
from .locators import LoginAdminPage
from .main_page import MainPage
from urllib.parse import urljoin


class LoginToAdminPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url = urljoin(driver.browser_base_url, '/administration')

    def login(self) -> 'AdminPage':
        self._driver.find_element(*LoginAdminPage.FIRST_NAME_INPUT).send_keys('user')
        self._driver.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys('bitnami')
        self._driver.find_element(*LoginAdminPage.LOGIN_BUTTON).click()

        return AdminPage(self._driver)
