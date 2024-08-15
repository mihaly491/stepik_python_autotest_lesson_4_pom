import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser chrome of firefox")
    parser.addoption('--language', action='store', default=None, help='Choose language')


@pytest.fixture(scope='function')
@pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
def browser(request):
    language = request.config.getoption("language")

    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    firefox_options = FirefoxOptions()
    firefox_options.set_preference('intl.accept_languages', language)
    firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

    # It didn't work for me without using Service on venv
    chrome_service = ChromeService(executable_path='C:/chromedriver-win64/chromedriver.exe',
                                   log_path='chromedriver.log')
    firefox_service = FirefoxService(executable_path='C:/geckodriver/geckodriver.exe', log_path='geckodriver.log')

    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_options, service=chrome_service)
    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox(options=firefox_options, service=firefox_service)
    else:
        print("\nbrowser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()
