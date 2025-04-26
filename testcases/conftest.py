import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Services for different browsers (Chrome, Edge, Firefox)
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# Driver managers for handling browser drivers automatically
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Utilities (for logging)
from utilities.utils import Utils


# Add options to pytest command-line arguments
def pytest_addoption(parser):
    # Define options for specifying the browser and URL
    parser.addoption("--browser", action="store", default="edge", help="Specify the browser to use (chrome, edge, firefox)")
    parser.addoption("--url", action="store", default="https://www.yatra.com/", help="Application URL")


# Fixture to get the browser type from the command line argument
@pytest.fixture(scope="class")
def browser(request):
    # Retrieve the browser type specified via the command line option (default is 'edge')
    return request.config.getoption("--browser")


# Fixture to get the URL from the command line argument
@pytest.fixture(scope="class")
def url(request):
    # Retrieve the application URL specified via the command line option (default is 'https://www.yatra.com/')
    return request.config.getoption("--url")


# Setup fixture that runs before each test class
@pytest.fixture(scope="class", autouse=True)
def setup(request, browser, url):
    # Create a custom logger instance
    log = Utils.custom_logger(logging.INFO)

    # Select the browser based on the user's input
    if browser.lower() == "chrome":
        log.info("Opening Chrome Browser")
        # Initialize Chrome browser and driver manager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser.lower() == "edge":
        log.info("Opening Edge Browser")
        # Initialize Edge browser and driver manager
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser.lower() == "firefox":
        log.info("Opening Firefox Browser")
        # Initialize Firefox browser and driver manager
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        # Raise an exception if the browser is not supported
        raise Exception(f"Browser {browser} is not supported.")

    # Open the application URL
    driver.get(url)
    # Maximize the browser window
    driver.maximize_window()

    # Set the driver and wait time for the test class
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 5)

    # Yield the driver to allow tests to run after setup
    yield driver

    # After the test completes, close the browser
    log.info("Closing the browser")
    driver.quit()
