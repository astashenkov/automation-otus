import pytest

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


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
def session(request):
    browser_name = request.config.getoption('browser').lower()

    match browser_name:
        case 'chrome':
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        case 'firefox':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        case 'safari':
            driver = webdriver.Safari()
        case 'opera':
            webdriver_service = service.Service(OperaDriverManager().install())
            webdriver_service.start()

            options = webdriver.ChromeOptions()
            options.add_experimental_option('w3c', True)

            driver = webdriver.Remote(webdriver_service.service_url, options=options)
        case 'edge':
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        case _:
            raise ValueError(f'Unsupported browser: {browser_name}')

    driver.browser_base_url = request.config.getoption('url')
    driver.maximize_window()

    yield driver

    driver.quit()
