import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        help='Choose browser: Chrome, FireFox, Safari or Edge.')


@pytest.fixture()
def browser(request):
    CHROMEDRIVER_PATH = 'drivers/chromedriver'
    FIREFOXDRIVER_PATH = 'drivers/geckodriver'
    EDGEDRIVER_PATH = 'drivers/'
    browser_name = request.config.getoption('browser')

    match browser_name:
        case 'chrome':
            options = ChromeOptions()
            options.page_load_strategy = 'normal'
            service = ChromeService(executable_path=CHROMEDRIVER_PATH)
            driver = webdriver.Chrome(service=service, options=options)
        case 'firefox':
            options = FirefoxOptions()
            options.page_load_strategy = 'normal'
            service = FirefoxService(executable_path=FIREFOXDRIVER_PATH)
            driver = webdriver.Firefox(service=service, options=options)
        case 'safari':
            options = SafariOptions()
            options.page_load_strategy = 'normal'
            service = SafariService()
            driver = webdriver.Safari(service=service, options=options)
        case 'edge':
            options = EdgeOptions()
            options.page_load_strategy = 'normal'
            service = EdgeService(executable_path=EDGEDRIVER_PATH)
            driver = webdriver.Edge(service=service, options=options)
        case _:
            raise ValueError(f'Unsupported browser: {browser_name}')

    driver.maximize_window()
    yield driver
    driver.quit()
