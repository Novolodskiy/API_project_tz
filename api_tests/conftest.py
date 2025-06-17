import pytest
from api_tests.endpoints.get_users import GetUsersEndpoint
from api_tests.endpoints.get_user_by_id import GetUserByIdEndpoint

ENDPOINTS = {
    'get_users': GetUsersEndpoint,
    'get_user_by_id': GetUserByIdEndpoint
}

@pytest.fixture(scope='session')
def get_existing_ids():
    endpoint = GetUsersEndpoint()
    response = endpoint.send_request(gender='male')
    endpoint.check_status_code(response, 200)
    data = response.json()
    return data.get('idList', [])

@pytest.fixture(scope='session')
def get_non_existing_id(get_existing_ids):
    return max(get_existing_ids) + 1 if get_existing_ids else 9999

@pytest.fixture(scope='function')
def get_endpoint_class():
    def _factory(name):
        return ENDPOINTS[name]()
    return _factory
