import logging
import time
from selenium.webdriver.common.by import By
import pytest
from utilities.utils import Utils
from base.base_driver import base_driver


class search_flight_page(base_driver):
    # Create a logger instance with INFO logging level
    log = Utils.custom_logger(logging_level=logging.INFO)

    def __init__(self, driver, wait):
        # Initialize the base driver and set up the driver and wait time for the current page
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def switch_to_alert(self):
        # Switch to browser alert (e.g., pop-up) and dismiss it (close the alert)
        alert_switch = self.driver.switch_to.alert()
        alert_switch.dismiss()

    #   Locators for different flight filters (1 Stop, 2 Stops, and 0 Stops)
    filter_by_one_stop = "//p[normalize-space()='1']"
    filter_by_two_stop = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    filter_by_zero_stop = "//p[@class='font-lightgrey bold'][normalize-space()='0']"

    # Method to locate the "1 Stop" filter
    def filter_one_stop(self):
        return self.presence_of_element_located(By.XPATH, self.filter_by_one_stop)

    # Method to locate the "2 Stop" filter
    def filter_two_stop(self):
        return self.presence_of_element_located(By.XPATH, self.filter_by_two_stop)

    # Method to locate the "No Stop" filter
    def filter_zero_stop(self):
        return self.presence_of_element_located(By.XPATH, self.filter_by_zero_stop)

    # Method to filter flights based on the number of stops (1, 2, or No Stop)
    def filter_by_stop(self, by_stop):
        # If "1 Stop" is selected, click the corresponding filter and log the action
        if by_stop == "1 Stop":
            self.filter_one_stop().click()
            self.log.warning("1 Stop Filtered")
            time.sleep(2)  # Pause for 2 seconds to allow page to update

        # If "2 Stop" is selected, click the corresponding filter and log the action
        elif by_stop == "2 Stop":
            self.filter_two_stop().click()
            self.log.warning("2 Stop Filtered")
            time.sleep(2)  # Pause for 2 seconds to allow page to update

        # If "No Stop" is selected, click the corresponding filter and log the action
        elif by_stop == "No Stop":
            self.filter_zero_stop().click()
            self.log.warning("0 Stop Filtered")
            time.sleep(2)  # Pause for 2 seconds to allow page to update

        # If an invalid option is provided, print an error message
        else:
            print("Enter Valid stop")

    # Method to count the number of flight results displayed on the search results page
    def all_flights_in_search_flight_page(self):
        # Find all the flight elements with the class "js-flightItem" (flight items on the page)
        all_flights = self.presence_of_elements_located(By.CLASS_NAME, "js-flightItem")

        # Log the total number of flights found on the page
        self.log.info(f"Total number of flights in the search flight page is %s", len(all_flights))
