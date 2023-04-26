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


class CatalogPageLocators:
    COMPARE_BUTTON = (By.CSS_SELECTOR, '#compare-total')
    PAGE_PAGINATION = (By.CSS_SELECTOR, '.pagination')
    SORT_BY_BUTTON = (By.XPATH, '//*[@for="input-sort"]')
    SHOW_BUTTON = (By.XPATH, '//*[@for="input-limit"]')
    GRID_BUTTON = (By.CSS_SELECTOR, '#button-grid')


class ProductCardPageLocators:
    PRODUCT_IMAGE = (By.CSS_SELECTOR, '.image.magnific-popup')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '#input-quantity')
    OPTIONS_DROPDOWN = (By.CSS_SELECTOR, '#input-option-226')
    DESCRIPTION_TAB = (By.CSS_SELECTOR, '#tab-description')


class LoginAdminPage:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
