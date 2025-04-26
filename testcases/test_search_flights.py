import logging
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.search_flight_page import search_flight_page
from pages.yatra_launch_page import Launching_page
from utilities.utils import Utils


# This fixture runs automatically after each test case
@pytest.fixture(autouse=True)
def wait_after_test():
    yield  # Test executes before this line
    time.sleep(5)  # Wait 5 seconds after the test


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilters:
    log = Utils.custom_logger(logging_level=logging.INFO)
    def test_search_flight(self):
        # Set an implicit wait for element availability
        self.wait = WebDriverWait(self.driver, 10)
        # Create an object of the Launching_page to interact with the homepage
        lp = Launching_page(self.driver, self.wait)
        # Enter the departure city
        lp.depart_field_selection()
        lp.depart_from_loc("Dubai")
        # Enter the destination city
        lp.going_to_field_selection()
        lp.going_to_loc("Hyderabad")
        # Select the desired travel date
        lp.depart_calender_date_selection()
        # Click on the search button to find flights
        search_button = lp.search_selection_in_homepage()
        # Scroll the search results page to trigger dynamic content
        lp.page_scroll()
        # Create an object for the flight search results page
        # search_flight = search_flight_page(self.driver, self.wait)
        # Apply the filter for 1-stop flights
        search_button.filter_by_stop("1 Stop")
        # search_button.filter_by_stop("2 Stop")
        # search_button.filter_by_stop("No Stop")
        search_button.all_flights_in_search_flight_page()
