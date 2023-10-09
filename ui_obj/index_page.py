from utils.auto_tester import AutoTester
from selenium.webdriver.common.by import By
import logging

class IndexPage(AutoTester):
    
    _about_us_xpath_locator = (By.XPATH, "//a[contains(@href,'about.htm')")
    _about_us_title_locator = (By.CLASS_NAME, "title")
    
    


    def __init__(self):
        super().__init__()
        self.driver = None
        self.db = None


    def click_about_us(self):
        logging.info('Go to about us...')
        self.click(self._about_us_xpath_locator)

    def get_about_us_title(self):
        logging.info('Checking if title is correctly displayed...')
        return self.get_element(self._about_us_title_locator).text