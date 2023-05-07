from urllib.parse import urljoin

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import LoginAdminPageLocators
from .main_page import MainPage
from .admin_page import AdminPage


class LoginToAdminPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url = urljoin(driver.browser_base_url, '/administration')

    @allure.step('Logging in to my admin account')
    def login(self) -> 'AdminPage':
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(LoginAdminPageLocators.FIRST_NAME_INPUT)
        ).send_keys('user')
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(LoginAdminPageLocators.PASSWORD_INPUT)
        ).send_keys('bitnami')
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(LoginAdminPageLocators.LOGIN_BUTTON)
        ).click()
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#column-left'))
        )

        return AdminPage(self._driver, self._driver.current_url)
