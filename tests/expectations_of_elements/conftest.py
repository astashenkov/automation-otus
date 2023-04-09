import pytest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        help='Choose browser: chrome, firefox, opera, safari, edge, yandex'
    )


@pytest.fixture()
def browser(request) -> WebDriver:
    browser_name = request.config.getoption('browser')

    match browser_name:
        case 'chrome':
            driver: WebDriver = webdriver.Chrome('drivers/chromedriver')
        case 'firefox':
            driver: WebDriver = webdriver.Firefox()
        case 'opera':
            driver: WebDriver = webdriver.Opera()
        case 'safari':
            driver: WebDriver = webdriver.Safari()
        case 'edge':
            driver: WebDriver = webdriver.Edge()
        case 'yandex':
            driver: WebDriver = webdriver.Chrome()
        case _:
            raise ValueError(f'Unsupported browser: {browser_name}')

    yield driver
    driver.quit()
