from selenium.webdriver.common.by import By
from utils.auto_tester import AutoTester
import time
from selenium.webdriver.common.by import By
import logging




class IndexPage(AutoTester):
    
    about_us_locator = (By.XPATH, "//a[contains(@href,'about.htm')]")
    title_locator = (By.CLASS_NAME, "title")
    


    def __init__(self, driver):
        super().__init__(driver)

    def click_about_us(self):
        logging.info('Going to about us ...')
        self.click(self.about_us_locator)
    
    def get_about_us_title(self):
        logging.info('Getting title ...')
        return self.get_element(self.title_locator).text