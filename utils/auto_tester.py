from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import logging
class AutoTester:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, y):
        self.driver.execute_script(f"window.scrollTo(0, {y})")
        

    def get_element(self, locator, **kwargs):
        if 'clickable' in kwargs.keys() and kwargs['clickable'] == True:
            return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))



    def get_elements(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))
    

    def input(self, text, locator):
        ele = self.get_element(locator, clickable=True)
        ele.clear()
        ele.send_keys(text)
        ele.send_keys(Keys.ENTER)


    def click(self, locator):
        ele = self.get_element(locator, clickable=True)
        ele.click()



    def check_alert(self):
        logging.info('Getting message info...')
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())

            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        
        except TimeoutException:
            print("no alert")


    def get_token(self):
        token = self.driver.execute_script("return window.localStorage.getItem('jwtToken');")
        logging.info('Getting token...')
        self.token = token
        return token

    def save_token(self, key, value):
         logging.info(f'Save token to local storage...')
         self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

    def add_new_tab_to_record(self, tab_name):
        for handle in self.driver.window_handles:
            if handle not in self.tab.values():
                self.tab[tab_name] = handle
        """
        檢查目前所有的分頁有沒有都在self.tab這個dict中
        沒有就新增指定的tab名稱鍵值對
        value存handle

        為了方便撰寫
        只會加入最後查撿到的一筆
        """


    def switch_tab_to(self, tab_name):
        self.driver.switch_to.window(self.tab[tab_name])
        

    def input_iframe(self, text, locator, iframe_locator):
        iframe = self.get_element(iframe_locator)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*locator).send_keys(text)
        self.driver.switch_to.default_content()
