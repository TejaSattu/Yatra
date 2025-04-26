import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Services
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# Drivers
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Utilities
from utilities.utils import Utils


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge")
    parser.addoption("--url")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class")
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    log = Utils.custom_logger(logging.INFO)

    if browser == "chrome":
        log.info("Opening Chrome Browser")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "edge":
        log.info("Opening Edge Browser")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        log.info("Opening Firefox Browser")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise Exception(f"Browser {browser} is not supported.")

    driver.get(url)
    driver.maximize_window()

    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 5)

    yield driver

    log.info("Closing the browser")
    driver.quit()
