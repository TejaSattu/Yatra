import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from base.base_driver import base_driver
from pages.search_flight_page import search_flight_page


# ---------------------------
# Page Object Class for Launch Page (Flight Search Page)
# ---------------------------
class Launching_page(base_driver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # ---------------------------
    # Locators (elements on the page)
    # ---------------------------
    DEPART_FROM_FIELD_SELECTION = "//p[@title='New Delhi']"
    DEPART_FROM_TEXT_FIELD_SELECTION = "//*[@id='input-with-icon-adornment']"
    SEARCH_DEPART_DROPDOWN_SELECTION = "//div[normalize-space()='Dubai, (DXB)']"

    GOING_TO_FIELD = "//p[@title='Mumbai']"
    GOING_TO_TEXT_SELECTION = "input-with-icon-adornment"
    SEARCH_GOING_DROPDOWN_SELECTION = "//div[@class='fw-600 mb-0']"

    DEPART_CALENDER_FIELD_SELECTION = "//div[@class='css-w7k25o']"
    # DEPART_CALENDER_SELECTION = "//div[@class='MuiBox-root css-89knyc']"
    DEPART_DATE_SELECTION_FROM_CALENDER = "(//span[@aria-label='MAHA SHIVARATHIRI'])[67]"
    CLICKING_SEARCH = "(//button[normalize-space()='Search'])[1]"

    # ---------------------------
    # Methods to perform actions
    # ---------------------------

    def depart_field_selection(self):
        """Click on the 'Depart From' field to activate the text input."""
        return self.element_to_be_clickable(By.XPATH, self.DEPART_FROM_FIELD_SELECTION).click()

    def DEPART_FROM_LOCATION_SELECTION(self):
        """Locate the text input field for departure location."""
        return self.element_to_be_clickable(By.XPATH, self.DEPART_FROM_TEXT_FIELD_SELECTION)

    def depart_from_loc(self, departure_location):
        """Enter the departure location and select from dropdown."""
        self.DEPART_FROM_LOCATION_SELECTION().click()
        self.DEPART_FROM_LOCATION_SELECTION().send_keys(departure_location)
        self.DEPART_FROM_LOCATION_SELECTION().send_keys(Keys.ENTER)
        time.sleep(2)  # Allow dropdown to load
        self.element_to_be_clickable(By.XPATH, self.SEARCH_DEPART_DROPDOWN_SELECTION).click()

    def going_to_field_selection(self):
        """Click on the 'Going To' field to activate the destination input."""
        return self.element_to_be_clickable(By.XPATH, self.GOING_TO_FIELD).click()

    def GOING_LOCATION_TEXTBOX_SELECTION(self):
        """Locate the text input field for destination location."""
        return self.element_to_be_clickable(By.ID, self.GOING_TO_TEXT_SELECTION)

    def going_to_loc(self, going_to):
        """Enter the destination location and select from dropdown."""
        self.GOING_LOCATION_TEXTBOX_SELECTION().click()
        self.GOING_LOCATION_TEXTBOX_SELECTION().send_keys(going_to)
        self.GOING_LOCATION_TEXTBOX_SELECTION().send_keys(Keys.ENTER)
        time.sleep(2)  # Allow dropdown to load
        self.element_to_be_clickable(By.XPATH, self.SEARCH_GOING_DROPDOWN_SELECTION).click()

    def depart_calender_date_selection(self):
        """Open the calendar and select the departure date."""
        self.element_to_be_clickable(By.XPATH, self.DEPART_CALENDER_FIELD_SELECTION).click()
        # self.element_to_be_clickable(By.XPATH, self.DEPART_CALENDER_SELECTION).click()
        self.presence_of_element_located(By.XPATH, self.DEPART_DATE_SELECTION_FROM_CALENDER).click()

    def search_selection_in_homepage(self):
        """Click on the Search button and return SearchFlightPage object."""
        self.presence_of_element_located(By.XPATH, self.CLICKING_SEARCH).click()
        search_flight_page_window = search_flight_page(self.driver, self.wait)
        return search_flight_page_window

    def search_flight(self, departure_location, going_to):
        """Helper method to perform the entire search flight operation."""
        self.depart_from_loc(departure_location)
        self.going_to_loc(going_to)
