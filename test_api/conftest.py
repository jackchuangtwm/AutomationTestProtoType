import pytest
from dotenv import load_dotenv
import os
import requests
import logging
from test_data.get_data_from_excel import ExcelSheetOperator

if 'ENV_FILE' in os.environ:
    env_file = os.environ['ENV_FILE']
    load_dotenv(env_file)
else:
    load_dotenv()

excel_reader = ExcelSheetOperator(file_name='test_data/test_data.xlsx', sheet_name='Login_info_data')
login_info_dict_list = excel_reader.to_dict_list()

@pytest.fixture()
def create_session():
    session = requests.session()
    yield session
    session.close()


@pytest.fixture()
def login_api(create_session, worker_id):
    session = create_session

    logging.info(f'worker_id : {worker_id}')

    account, password, return_code = (
        login_info_dict_list[int(worker_id.split("w")[1])]['Account'],
        login_info_dict_list[int(worker_id.split("w")[1])]['Password'],
        login_info_dict_list[int(worker_id.split("w")[1])]['Return code'],
    )
    login_response = session.get(url=f'{os.getenv("API_DOMAIN")}/{account}/{password}')
    
    assert int(login_response.status_code) == int(return_code), f'Expected login response code : {return_code}, got : {login_response.status_code}'
    yield
