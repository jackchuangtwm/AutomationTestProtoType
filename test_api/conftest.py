import pytest
from dotenv import load_dotenv
import os
import requests
import logging


if 'ENV_FILE' in os.environ:
    env_file = os.environ['ENV_FILE']
    load_dotenv(env_file)
else:
    load_dotenv()


@pytest.fixture()
def create_session():
    session = requests.session()
    yield session
    session.close()


@pytest.fixture()
def login_api(create_session, request, worker_id):
    session = create_session

    logging.info(f'worker_id : {worker_id}')

    account, password, return_code = request.param
    password = os.getenv(password)
    return_code = int(return_code)

    # if worker_id == 'gw0':
    #     account = 'HomeSimpsons'

    login_response = session.get(url=f'{os.getenv("API_DOMAIN")}/{account}/{password}')
    
    assert int(login_response.status_code) == int(return_code), f'Expected login response code : {return_code}, got : {login_response.status_code}'
    yield login_response
