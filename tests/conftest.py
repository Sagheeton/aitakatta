# импорты для set_web_deriver *****************************

import chromedriver_autoinstaller
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# *********************************************************


# чтобы не было красной ошибки от webdriver-manager'a *****
@pytest.fixture(scope="session", autouse=True)
def set_web_driver():
    s = chromedriver_autoinstaller.install()
    browser.config.driver = webdriver.Chrome(service=Service(s))
    browser.config.driver.set_window_size(1920, 1080)
# *********************************************************


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.hold_browser_open = True
