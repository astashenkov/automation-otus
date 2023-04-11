import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        help='Choose browser: Chrome, FireFox, Safari or Edge.'
    )
    parser.addoption(
        '--url',
        default='https://www.opencart.com/',
        help='Choose base URL.'
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser')

    match browser_name:
        case 'chrome':
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        case 'firefox':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        case 'safari':
            driver = webdriver.Safari()
        case 'edge':
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        case _:
            raise ValueError(f'Unsupported browser: {browser_name}')

    driver.maximize_window()
    yield driver
    driver.quit()
