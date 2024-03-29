from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CurrencySwitcher:
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '.nav.float-start>.list-inline')
    CHOSE_DOLLAR = (By.CSS_SELECTOR, '[href = "USD"]')
    CHOSE_POUND = (By.CSS_SELECTOR, '[href = "GBP"')
    CHOSE_EURO = (By.CSS_SELECTOR, '[href = "EUR"')
    SELECTED_CURRENCY = (By.CSS_SELECTOR, '.nav.float-start>.list-inline strong')

    def __init__(self, driver):
        self._driver = driver

    def open_dropdown(self):
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(self.CURRENCY_DROPDOWN)
        ).click()

    def choose_euro(self):
        self.open_dropdown()
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(self.CHOSE_EURO)
        ).click()

    def choose_pound(self):
        self.open_dropdown()
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(self.CHOSE_POUND)
        ).click()

    def choose_dollar(self):
        self.open_dropdown()
        WebDriverWait(self._driver, 2).until(
            EC.presence_of_element_located(self.CHOSE_DOLLAR)
        ).click()

    @property
    def selected_currency(self):
        selected = self._driver.find_element(*self.SELECTED_CURRENCY).text
        if selected == '£':
            return 'Pound'
        elif selected == '€':
            return 'Euro'
        elif selected == '$':
            return 'Dollar'
        else:
            return ''
