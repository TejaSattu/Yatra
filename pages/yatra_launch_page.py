import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from base.base_driver import base_driver
from pages.search_flight_page import search_flight_page


class Launching_page(base_driver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    DEPART_FROM_FIELD_SELECTION = "//*[@id='__next']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/p[2]"
    DEPART_FROM_TEXT_FIELD_SELECTION = "//*[@id='input-with-icon-adornment']"
    SEARCH_DEPART_DROPDOWN_SELECTION = "//*[@id='__next']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div/ul/div/li"
    GOING_TO_FIELD = "//*[@id='__next']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/p[2]"
    GOING_TO_TEXT_SELECTION = "input-with-icon-adornment"
    SEARCH_GOING_DROPDOWN_SELECTION = "//*[@id='__next']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/ul/div[1]/li"
    DEPART_CALENDER_FIELD_SELECTION = "//*[@id='__next']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]"
    DEPART_CALENDER_SELECTION = "//*[@id='__next']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[4]"
    # MAY 7th 2025
    DEPART_DATE_SELECTION_FROM_CALENDER = "//div[@aria-label='Choose Wednesday, May 7th, 2025']"
    CLICKING_SEARCH = "//*[@id='__next']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[4]/div"

    def depart_field_selection(self):
        return self.element_to_be_clickable(By.XPATH,
                                            self.DEPART_FROM_FIELD_SELECTION).click()

    def DEPART_FROM_LOCATION_SELECTION(self):
        return self.element_to_be_clickable(By.XPATH,
                                            self.DEPART_FROM_TEXT_FIELD_SELECTION)

    def depart_from_loc(self, departure_location):
        self.DEPART_FROM_LOCATION_SELECTION().click()
        self.DEPART_FROM_LOCATION_SELECTION().send_keys(departure_location)
        self.DEPART_FROM_LOCATION_SELECTION().send_keys(Keys.ENTER)
        time.sleep(2)
        self.element_to_be_clickable(By.XPATH, self.SEARCH_DEPART_DROPDOWN_SELECTION).click()

    def going_to_field_selection(self):
        return self.element_to_be_clickable(By.XPATH, self.GOING_TO_FIELD).click()

    def GOING_LOCATION_TEXTBOX_SELECTION(self):
        return self.element_to_be_clickable(By.ID, self.GOING_TO_TEXT_SELECTION)

    def going_to_loc(self, going_to):
        self.GOING_LOCATION_TEXTBOX_SELECTION().click()
        self.GOING_LOCATION_TEXTBOX_SELECTION().send_keys(going_to)
        self.GOING_LOCATION_TEXTBOX_SELECTION().send_keys(Keys.ENTER)
        time.sleep(2)
        self.element_to_be_clickable(By.XPATH, self.SEARCH_GOING_DROPDOWN_SELECTION).click()

    def depart_calender_date_selection(self):
        self.element_to_be_clickable(By.XPATH, self.DEPART_CALENDER_FIELD_SELECTION).click()
        self.element_to_be_clickable(By.XPATH, self.DEPART_CALENDER_SELECTION).click()
        self.presence_of_element_located(By.XPATH, self.DEPART_DATE_SELECTION_FROM_CALENDER).click()

    def search_selection_in_homepage(self):
        self.presence_of_element_located(By.XPATH, self.CLICKING_SEARCH).click()
        search_flight_page_window = search_flight_page(self.driver, self.wait)
        return search_flight_page_window

    def search_flight(self, departure_location, going_to):
        self.depart_from_loc(departure_location)
        self.going_to_loc(going_to)



