from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import logging
class AutoTester:

    def __init__(self, driver):
        self.driver = driver


    def get_element(self, locator, **kwargs):
        if 'clickable' in kwargs.keys() and kwargs['clickable'] == True:
            return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        ele = self.get_element(locator, clickable=True)
        ele.click()