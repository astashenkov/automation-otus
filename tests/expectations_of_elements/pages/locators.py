from selenium.webdriver.common.by import By


class MainPageLocators:
    HERO_BANNER = (By.CSS_SELECTOR, '#hero')
    MARKETPLACE_SECTION = (By.CSS_SELECTOR, '#marketplace')
    BUSINESS_SECTION = (By.CSS_SELECTOR, '#business')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.navbar-btn.btn-link')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '.navbar-btn.btn-black')
