import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 5)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield driver
    driver.close()
