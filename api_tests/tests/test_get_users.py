import allure
import pytest
from api_tests.endpoints.get_users import GetUsersEndpoint

@allure.title("TC01 - gender=male")
def test_tc01_get_users_male(get_endpoint_class):
    endpoint = get_endpoint_class('get_users')
    response = endpoint.send_request(gender='male')
    endpoint.check_status_code(response, 200)
    endpoint.check_content_type(response)
    endpoint.check_success_true(response)
    endpoint.check_idlist_is_array(response)

@allure.title("TC02 - gender=magic")
def test_tc02_get_users_magic(get_endpoint_class):
    endpoint = get_endpoint_class('get_users')
    response = endpoint.send_request(gender='magic')
    endpoint.check_status_code(response, 400)
    endpoint.check_content_type(response)

@allure.title("TC03 - gender=McCloud")
def test_tc03_get_users_mccloud(get_endpoint_class):
    endpoint = get_endpoint_class('get_users')
    response = endpoint.send_request(gender='McCloud')
    endpoint.check_status_code(response, 400)
    endpoint.check_content_type(response)

@allure.title("TC04 - gender=female")
def test_tc04_get_users_female(get_endpoint_class):
    endpoint = get_endpoint_class('get_users')
    response = endpoint.send_request(gender='female')
    endpoint.check_status_code(response, 200)
    endpoint.check_content_type(response)
    endpoint.check_success_true(response)
    endpoint.check_idlist_is_array(response)

@allure.title("TC05 - gender=robot")
def test_tc05_get_users_robot(get_endpoint_class):
    endpoint = get_endpoint_class('get_users')
    response = endpoint.send_request(gender='robot')
    endpoint.check_status_code(response, 400)
    endpoint.check_content_type(response)

@allure.title("TC06 - no gender")
def test_tc06_get_users_no_gender(get_endpoint_class):
    endpoint = get_endpoint_class('get_users')
    response = endpoint.send_request()
    endpoint.check_status_code(response, 200)
    endpoint.check_content_type(response)
    endpoint.check_success_true(response)
    endpoint.check_idlist_is_array(response)

@allure.title("TC07 - gender empty")
def test_tc07_get_users_empty_gender(get_endpoint_class):
    endpoint = get_endpoint_class('get_users')
    response = endpoint.send_request(gender='')
    endpoint.check_status_code(response, 400)
    endpoint.check_content_type(response)

@allure.title("TC08 - gender=MALE")
def test_tc08_get_users_uppercase_gender(get_endpoint_class):
    endpoint = get_endpoint_class('get_users')
    response = endpoint.send_request(gender='MALE')
    endpoint.check_status_code(response, 200)
    endpoint.check_content_type(response)
    endpoint.check_success_true(response)
    endpoint.check_idlist_is_array(response)

@allure.title("TC09 - POST instead of GET")
def test_tc09_get_users_post(get_endpoint_class):
    endpoint = get_endpoint_class('get_users')
    response = endpoint.send_request(method='POST')
    endpoint.check_status_code(response, 405)
    endpoint.check_content_type(response)
