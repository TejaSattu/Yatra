
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep, time


class Test_login:
    def test_dst_search_box(self):
        driver = webdriver.Edge()
        driver.maximize_window()
        # # self.driver.implicitly_wait(5)
        # # wait = WebDriverWait(self.driver, 5)  # Increased wait time
        # # Click on "From" field
        # # from_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        # from_field = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        # from_field.click()
        # # Enter "New York" and wait for suggestions
        # from_field.send_keys("New York")
        # # Select first suggestion
        # from_field.send_keys(Keys.ENTER)

        going_to = driver.find_element(By.XPATH, "//label[@id='input-with-icon-adornment-label']")
        going_to.click()
        going_to.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//*[@id='__next']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div/ul/div/li[1]")
        print(len(search_results))

        for results in search_results:
            if "New York, (JFK)" in results.text:
                results.click()
                break


