import pytest
from ui_obj.index_page import IndexPage
from test_data.get_data_from_excel import ExcelSheetOperator
import os
import logging
# excel = ExcelSheetOperator(file_name='test_data/test_data.xlsx', sheet_name='Create Product Success')
# @pytest.mark.parametrize(
#         argnames='create_info_dict_list, index',
#         argvalues=[
#             (excel.to_dict(), i) for i in range(excel.row_count())
#         ]
# )

def test_about_us(set_driver):
    
    page_obj = IndexPage(set_driver)
    page_obj.driver.get(f'{os.getenv("DOMAIN")}')
    page_obj.click_about_us()
    title = page_obj.get_about_us_title()
    assert title == 'ParaSoft Demo Website', f'Expected : ParaSoft Demo Website, Got : {title}'


