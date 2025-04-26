import logging
import time
from selenium.webdriver.common.by import By
import pytest
from utilities.utils import Utils
from base.base_driver import base_driver


class search_flight_page(base_driver):

    log = Utils.custom_logger(logging_level=logging.INFO)

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def switch_to_alert(self):
        # Switch to browser alert and dismiss it (e.g., close pop-up alerts)
        alert_switch = self.driver.switch_to.alert()
        alert_switch.dismiss()

#   Locators

    filter_by_one_stop = "//p[normalize-space()='1']"
    filter_by_two_stop = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    filter_by_zero_stop = "//p[@class='font-lightgrey bold'][normalize-space()='0']"

    def filter_one_stop(self):
        return self.presence_of_element_located(By.XPATH, self.filter_by_one_stop)

    def filter_two_stop(self):
        return self.presence_of_element_located(By.XPATH, self.filter_by_two_stop)

    def filter_zero_stop(self):
        return self.presence_of_element_located(By.XPATH, self.filter_by_zero_stop)

    def filter_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.filter_one_stop().click()
            self.log.warning("1 Stop Filtered")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.filter_two_stop().click()
            self.log.warning("2 Stop Filtered")
            time.sleep(2)
        elif by_stop == "No Stop":
            self.filter_zero_stop().click()
            self.log.warning("0 Stop Filtered")
            time.sleep(2)
        else:
            print("Enter Valid stop")

    def all_flights_in_search_flight_page(self):

        all_flights = self.presence_of_elements_located(By.CLASS_NAME, "js-flightItem")
        self.log.info(f"Total number flight in the search flight page is %s", len(all_flights))



