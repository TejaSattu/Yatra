import time
import pytest
from selenium.webdriver.support import expected_conditions as EC


class base_driver:

    def __init__(self, driver, wait):
        # Initialize the driver instance
        self.driver = driver
        self.wait = wait

    def page_scroll(self):
        """
        Scrolls down the web page until the bottom is reached.
        This is useful for loading dynamic content that appears as the user scrolls.
        """
        lastCount = 0  # Stores the previous scroll height
        match = False  # Flag to check if the page has been fully scrolled

        while not match:
            # Scroll to the bottom and get the current scroll height
            page_length = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight"
            )

            # If scroll height hasn't changed, we've reached the bottom
            if lastCount == page_length:
                match = True
            else:
                lastCount = page_length  # Update the scroll height
                time.sleep(2)  # Wait for new content to load before scrolling again

    def element_to_be_clickable(self, locator, locator_type):

        list_of_elements = self.wait.until(
            EC.element_to_be_clickable((locator, locator_type)))

        return list_of_elements

    def presence_of_element_located(self, locator, locator_type):

        elements = self.wait.until(
            EC.presence_of_element_located((locator, locator_type)))
        return elements

    def presence_of_elements_located(self, locator, locator_type):

        number_of_elements = self.wait.until(
            EC.presence_of_all_elements_located((locator, locator_type)))
        return number_of_elements