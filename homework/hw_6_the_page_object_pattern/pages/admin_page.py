import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from .locators import AdminPageLocators


class AdminPage:
    def __init__(self, driver, url):
        self._driver = driver
        self._url = url

    @allure.step('Opening the product catalog')
    def open_products_page(self) -> None:
        self._driver.get(
            self._driver.current_url.replace('common/dashboard', 'catalog/product').replace('.form', '')
        )

    @allure.step('Removing the top product from the table')
    def delete_upper_product(self) -> str:
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.UPPER_PRODUCT_CHECKBOX)
        ).click()
        deleted_product_title = WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.UPPER_PRODUCT_TITLE)
        ).text
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.DELETE_BUTTON)
        ).click()
        Alert(self._driver).accept()
        time.sleep(1)  # Waiting for products to be updated in the table after deleting the top one

        return deleted_product_title

    @allure.step('Creating a new product')
    def create_new_product(self):
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.ADD_NEW_PRODUCT_BUTTON)
        ).click()
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.PRODUCT_NAME_INPUT)
        ).send_keys('Test product title')
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.META_TAG_TITLE)
        ).send_keys('Test meta tag title')
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.DATA_TAB)
        ).click()
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.INPUT_MODEL)
        ).send_keys('Test model')
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.SEO_TAB)
        ).click()
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.INPUT_KEYWORD)
        ).send_keys('Test')
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.SUBMIT_CREATE_PRODUCT_BUTTON)
        ).click()

    @property
    def upper_product_title(self) -> str:
        return WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(AdminPageLocators.UPPER_PRODUCT_TITLE)
        ).text
