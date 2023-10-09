import pytest
import pymysql
from dotenv import load_dotenv
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType




@pytest.fixture()
def set_driver():

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('', options=chrome_options)
    driver.set_window_size(2560, 1440)
    driver.get(os.getenv('DOMAIN'))
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()