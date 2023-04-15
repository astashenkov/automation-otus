from selenium.webdriver.common.by import By


class MainPageLocators:
    CAROUSEL_BANNER = (By.CSS_SELECTOR, '#carousel-banner-0')
    LOGO_MAIN = (By.CSS_SELECTOR, '#logo')
    PAGE_HEADER = (By.CSS_SELECTOR, '#top')
    CART_ITEMS = (By.CSS_SELECTOR, '[type="button"].btn-block')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[name="search"]')


class RegisterPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    SUBMIT_BUTTON = (By.XPATH, '//*[@type="submit"]')
