import pytest
import pymysql
from dotenv import load_dotenv
import os
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType

if 'ENV_FILE' in os.environ:
    env_file = os.environ['ENV_FILE']
    load_dotenv(env_file)
else:
    load_dotenv()


@pytest.fixture()
def set_driver():

    firefox_options = Options()
    # firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(2560, 1440)
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()