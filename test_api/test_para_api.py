from test_data.get_data_from_excel import ExcelSheetOperator
import pytest

excel_reader = ExcelSheetOperator(file_name='test_data/test_data.xlsx', sheet_name='Login_info_data')
login_info_dict_list = excel_reader.to_dict_list()

@pytest.mark.parametrize(
        argnames='login_api',
        argvalues=[info.values() for info in login_info_dict_list],
        indirect=['login_api']
)

def test_login(login_api):
    login_response = login_api
    