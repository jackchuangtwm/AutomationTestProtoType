from ui_obj.index_page import IndexPage
import os


def test_about_us(set_driver):
    
    page_obj = IndexPage(set_driver)
    page_obj.driver.get(f'{os.getenv("UI_DOMAIN")}')
    page_obj.click_about_us()
    title = page_obj.get_about_us_title()
    assert title == 'ParaSoft Demo Website', f'Expected : ParaSoft Demo Website, Got : {title}'


