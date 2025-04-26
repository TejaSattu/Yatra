import logging
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait

# Import Page Object classes
from pages.search_flight_page import search_flight_page
from pages.yatra_launch_page import Launching_page

# Import Utility class for custom logging
from utilities.utils import Utils

# ---------------------------
# Fixture to wait after each test (for UI stability)
# ---------------------------
@pytest.fixture(autouse=True)
def wait_after_test():
    """Fixture to wait after each test to ensure the browser settles before the next test."""
    yield
    time.sleep(5)  # Sleep for better stability when tests switch

# ---------------------------
# Test Class for Searching Flights and Verifying Filters
# ---------------------------
@pytest.mark.usefixtures("setup")  # Setup fixture will be automatically used
class TestSearchAndVerifyFilters:
    """Test case class to search flights and verify applied filters on Yatra website."""

    # Initialize custom logger
    log = Utils.custom_logger(logging_level=logging.INFO)

    def test_search_flight(self, setup):
        """Test to search flights between two cities and apply '1 Stop' filter."""

        self.log.info("===== STARTING TEST: Search Flight and Apply Filters =====")

        # Initialize Page Objects
        self.wait = WebDriverWait(self.driver, 10)
        launch_page = Launching_page(self.driver, self.wait)

        # ---------------------------
        # Step 1: Select Departure City
        # ---------------------------
        self.log.info("Step 1: Selecting departure city 'Dubai'")
        launch_page.depart_field_selection()
        launch_page.depart_from_loc("Dubai")

        # ---------------------------
        # Step 2: Select Destination City
        # ---------------------------
        self.log.info("Step 2: Selecting destination city 'Hyderabad'")
        launch_page.going_to_field_selection()
        launch_page.going_to_loc("Hyderabad")

        # ---------------------------
        # Step 3: Select Departure Date
        # ---------------------------
        self.log.info("Step 3: Selecting departure date")
        launch_page.depart_calender_date_selection()

        # ---------------------------
        # Step 4: Search for Flights
        # ---------------------------
        self.log.info("Step 4: Clicking on 'Search Flights'")
        search_page = launch_page.search_selection_in_homepage()

        # ---------------------------
        # Step 5: Scroll to Load All Search Results
        # ---------------------------
        self.log.info("Step 5: Scrolling the page to load results")
        launch_page.page_scroll()

        # ---------------------------
        # Step 6: Apply '1 Stop' Filter
        # ---------------------------
        self.log.info("Step 6: Applying '1 Stop' filter")
        search_page.filter_by_stop("1 Stop")

        # ---------------------------
        # Step 7: Validate Flights after Filter
        # ---------------------------
        self.log.info("Step 7: Validating all filtered flights")
        search_page.all_flights_in_search_flight_page()

        self.log.info("===== TEST COMPLETED SUCCESSFULLY =====")
        self.log.info("******* ============================ *******")
