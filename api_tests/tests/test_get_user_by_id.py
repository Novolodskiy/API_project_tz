import allure
import pytest
from api_tests.endpoints.get_user_by_id import GetUserByIdEndpoint

@allure.title("TC010 - existing id")
def test_tc010_get_user_existing(get_existing_ids, get_endpoint_class):
    user_id = get_existing_ids[0]
    endpoint = get_endpoint_class('get_user_by_id')
    response = endpoint.send_request(user_id)
    endpoint.check_status_code(response, 200)
    endpoint.check_content_type(response)
    endpoint.check_success_true(response)

@allure.title("TC011 - POST instead of GET by id")
def test_tc011_post_instead_get_by_id(get_existing_ids, get_endpoint_class):
    user_id = get_existing_ids[0]
    endpoint = get_endpoint_class('get_user_by_id')
    response = endpoint.send_request(user_id, method='POST')
    endpoint.check_status_code(response, 405)
    endpoint.check_content_type(response)

@allure.title("TC012 - non-existing id")
def test_tc012_get_user_non_existing(get_non_existing_id, get_endpoint_class):
    user_id = get_non_existing_id
    endpoint = get_endpoint_class('get_user_by_id')
    response = endpoint.send_request(user_id)
    endpoint.check_status_code(response, 404)
    endpoint.check_content_type(response)

@allure.title("TC013 - id as string")
def test_tc013_get_user_id_string(get_endpoint_class):
    endpoint = get_endpoint_class('get_user_by_id')
    response = endpoint.send_request('abc')
    endpoint.check_status_code(response, 400)
    endpoint.check_content_type(response)

@allure.title("TC014 - id=0")
def test_tc014_get_user_id_zero(get_endpoint_class):
    endpoint = get_endpoint_class('get_user_by_id')
    response = endpoint.send_request(0)
    endpoint.check_status_code(response, 400)
    endpoint.check_content_type(response)

@allure.title("TC015 - id=-1")
def test_tc015_get_user_negative_id(get_endpoint_class):
    endpoint = get_endpoint_class('get_user_by_id')
    response = endpoint.send_request(-1)
    endpoint.check_status_code(response, 400)
    endpoint.check_content_type(response)
