from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    This is a class with locators for main page.
    Here you can find locators for main logo, header of page, "search" input,
    "curt items" link and carousel banner.
    """
    CAROUSEL_BANNER = (By.CSS_SELECTOR, '#carousel-banner-0')
    CART_ITEMS = (By.CSS_SELECTOR, '[type="button"].btn-block')
    LOGO_MAIN = (By.CSS_SELECTOR, '#logo')
    PAGE_HEADER = (By.CSS_SELECTOR, '#top')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[name="search"]')


class RegisterPageLocators:
    """
    This is a class with locators for register page.
    Here you can find locators for "first name", "last name", "email" and "password" inputs.
    There is also a locator for the submit register button.
    """
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PRIVACY_POLICY = (By.CSS_SELECTOR, '[name="agree"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@type="submit"]')
    SUCCESS_MESSAGE = (By.XPATH, '//*[contains(text(), "account has been successfully created")]')


class CatalogPageLocators:
    """
    This is a class with locators for catalog page.
    Here you can find locators for "compare", "sort by", "show", "list" and "grid" buttons.
    """
    COMPARE_BUTTON = (By.CSS_SELECTOR, '#compare-total')
    GRID_BUTTON = (By.CSS_SELECTOR, '#button-grid')
    LIST_BUTTON = (By.CSS_SELECTOR, '#button-list')
    SHOW_BUTTON = (By.XPATH, '//*[@for="input-limit"]')
    SORT_BY_BUTTON = (By.XPATH, '//*[@for="input-sort"]')


class ProductCardPageLocators:
    """
    This is a class with locators for product card page.
    Here you can find locators for go to the description and review tabs, quantity input,
    "add to cart" button and image of a product.
    """
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')
    DESCRIPTION_TAB = (By.CSS_SELECTOR, '#tab-description')
    REVIEW_TAB = (By.CSS_SELECTOR, '#tab-review')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, '.image.magnific-popup')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '#input-quantity')


class LoginAdminPageLocators:
    """
    This is a class with locators for logging into the admin page.
    Here you can find locators for "first name" and "password" inputs,
    login button, "Forgot password" link, and "Go to home page" link.
    """
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    LOGIN_BUTTON = (By.XPATH, '//*[@type="submit"]')
    OPENCART_LINK = (By.XPATH, '//*[text()="OpenCart"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')


class AdminPageLocators:
    """
    This is a class with locators for the admin page.
    Here you can find locators for adding, removing and selecting products.
    """
    ADD_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, '.page-header .btn-primary:nth-child(2)')
    DATA_TAB = (By.CSS_SELECTOR, 'ul.nav-tabs li:nth-child(2)')
    DELETE_BUTTON = (By.CSS_SELECTOR, '.btn.btn-danger')
    INPUT_KEYWORD = (By.CSS_SELECTOR, '#input-keyword-0-1')
    INPUT_MODEL = (By.CSS_SELECTOR, '#input-model')
    META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title-1')
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '#input-name-1')
    SEO_TAB = (By.CSS_SELECTOR, 'ul.nav-tabs li:nth-child(11)')
    SUBMIT_CREATE_PRODUCT_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    UPPER_PRODUCT_CHECKBOX = (By.CSS_SELECTOR, '#form-product tbody td:nth-child(1) input')
    UPPER_PRODUCT_TITLE = (By.CSS_SELECTOR, '#form-product tbody td:nth-child(3)')
