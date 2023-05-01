from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    This is a class with locators for main page.
    Here you can find locators for main logo, header of page, "search" input,
    "curt items" link and carousel banner.
    """
    CAROUSEL_BANNER = (By.CSS_SELECTOR, '#carousel-banner-0')
    LOGO_MAIN = (By.CSS_SELECTOR, '#logo')
    PAGE_HEADER = (By.CSS_SELECTOR, '#top')
    CART_ITEMS = (By.CSS_SELECTOR, '[type="button"].btn-block')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[name="search"]')


class RegisterPageLocators:
    """
    This is a class with locators for register page.
    Here you can find locators for "first name", "last name", "email" and "password" inputs.
    There is also a locator for the submit register button.
    """
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PRIVACY_POLICY = (By.CSS_SELECTOR, '[name="agree"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@type="submit"]')
    SUCCESS_MESSAGE = (By.TAG_NAME, 'h1')


class CatalogPageLocators:
    """
    This is a class with locators for catalog page.
    Here you can find locators for "compare", "sort by", "show" and "grid" buttons.
    There is also a locator for the page pagination.
    """
    COMPARE_BUTTON = (By.CSS_SELECTOR, '#compare-total')
    PAGE_PAGINATION = (By.CSS_SELECTOR, '.pagination')
    SORT_BY_BUTTON = (By.XPATH, '//*[@for="input-sort"]')
    SHOW_BUTTON = (By.XPATH, '//*[@for="input-limit"]')
    GRID_BUTTON = (By.CSS_SELECTOR, '#button-grid')


class ProductCardPageLocators:
    """
    This is a class with locators for product card page.
    Here you can find locators for chose options, go to the description tab, quantity input,
    "add to cart" button and image of a product.
    """
    PRODUCT_IMAGE = (By.CSS_SELECTOR, '.image.magnific-popup')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '#input-quantity')
    OPTIONS_DROPDOWN = (By.CSS_SELECTOR, '#input-option-226')
    DESCRIPTION_TAB = (By.CSS_SELECTOR, '#tab-description')


class LoginAdminPage:
    """
    This is a class with locators for logging into the admin page.
    Here you can find locators for "first name" and "password" inputs,
    login button, "Forgot password" link, and "Go to home page" link.
    """
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    LOGIN_BUTTON = (By.XPATH, '//*[@type="submit"]')
    OPENCART_LINK = (By.XPATH, '//*[text()="OpenCart"]')


class AdminPage:
    """
    This is a class with locators for the admin page.
    Here you can find locators for adding, removing and selecting products.
    """
    DELETE_BUTTON = (By.CSS_SELECTOR, '[data-bs-original-title="Delete"]')
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, '[data-bs-original-title="Add New"]')
