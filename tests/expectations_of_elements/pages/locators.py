from selenium.webdriver.common.by import By


class MainPageLocators:
    HERO_BANNER = (By.CSS_SELECTOR, '#hero')
    MARKETPLACE_SECTION = (By.CSS_SELECTOR, '#marketplace')
    BUSINESS_SECTION = (By.CSS_SELECTOR, '#business')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.navbar-btn.btn-link')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '.navbar-btn.btn-black')


class RegisterPageLocators:
    WHY_JOIN_FRAME = (By.CSS_SELECTOR, '.well')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '#input-country')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '.btn-lg')
