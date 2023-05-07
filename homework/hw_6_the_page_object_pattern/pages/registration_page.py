import time

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib.parse import urljoin

from .locators import RegisterPageLocators
from .main_page import MainPage


class RegistrationPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url = urljoin(driver.browser_base_url, '/en-gb?route=account/register')

    @allure.step('Заполняю информацию о новом юзере')
    def fill_out_the_required_registration_data(self, *data) -> None:
        first_name, last_name, email, password = data
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(RegisterPageLocators.FIRST_NAME_INPUT)
        ).send_keys(first_name)
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(RegisterPageLocators.LAST_NAME_INPUT)
        ).send_keys(last_name)
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(RegisterPageLocators.EMAIL_INPUT)
        ).send_keys(email)
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(RegisterPageLocators.PASSWORD_INPUT)
        ).send_keys(password)

    @allure.step('Активирую чекбокс согласия с политикой безопасности')
    def activate_privacy_policy_checkbox(self) -> None:
        privacy_policy_checkbox = WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(RegisterPageLocators.PRIVACY_POLICY)
        )
        self._driver.execute_script("arguments[0].scrollIntoView();", privacy_policy_checkbox)
        privacy_policy_checkbox.send_keys(Keys.SPACE)

    @allure.step('Нажимаю кнопку Submit для регистрации юзера')
    def click_submit_button(self) -> None:
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(RegisterPageLocators.SUBMIT_BUTTON)
        ).click()

    @allure.step('Проверяю создан ли юзер')
    def is_success_created_account(self) -> bool:
        try:
            WebDriverWait(self._driver, 3).until(
                EC.presence_of_element_located(RegisterPageLocators.SUCCESS_MESSAGE)
            )
            return True
        except TimeoutError:
            return False
