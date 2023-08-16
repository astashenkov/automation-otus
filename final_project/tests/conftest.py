import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        help='Choose browser: Chrome, FireFox, Safari, Opera or Edge.'
    )
    parser.addoption(
        '--url',
        default='https://www.automationexercise.com/',
        help='Choose base URL'
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption('browser').lower()

    match browser_name:
        case 'chrome':
            driver = webdriver.Chrome()
        case 'firefox':
            driver = webdriver.Firefox()
        case 'safari':
            driver = webdriver.Safari()
        case 'edge':
            driver = webdriver.Edge()
        case _:
            raise ValueError(f'Unsupported browser: {browser_name}')

    driver.browser_base_url = request.config.getoption('url')
    driver.maximize_window()

    yield driver

    driver.quit()
