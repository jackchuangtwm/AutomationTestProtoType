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

    if hasattr(request, 'param'):
        logging.info('Login with request param from test case')
        email, password = request.param

    else:
        logging.info('Login with auto assigned credential')
        worker_id_num_part = str(int(worker_id.split("w")[1])+1)
        email, password = (
            os.getenv(f'MEMBER_EMAIL_{worker_id_num_part}'), 
            os.getenv(f'MEMBER_PASSWORD_{worker_id_num_part}')
            )
    
    login_request = {
                "provider": "native",
                "email": f"{email}",
                "password": f"{password}"
                }
    
    logging.info(f'Sending login request...\nLogin request = {str(login_request)}')
    login_response = session.post(url=f'{os.getenv("API_DOMAIN")}/user/login',data=login_request)
    
    if login_response.status_code == 200:
        session.headers = {"Authorization": f'Bearer {login_response.json()["data"]["access_token"]}'}
        
    logging.info(f'Login response = {str(login_response)}')
    yield session, login_response, login_request
