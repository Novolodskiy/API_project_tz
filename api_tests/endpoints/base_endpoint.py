import requests
import allure

class BaseEndpoint:
    BASE_URL = "http://example.com/api/test"

    def send_request(self, method, path="", params=None, json=None):
        url = f"{self.BASE_URL}/{path}".rstrip('/')
        with allure.step(f"Send {method} request to {url}"):
            response = requests.request(method, url, params=params, json=json)
        return response

    @allure.step("Check status code is {expected}")
    def check_status_code(self, response, expected):
        assert response.status_code == expected, (
            f"Expected status {expected}, got {response.status_code}")

    @allure.step("Check Content-Type is application/json")
    def check_content_type(self, response):
        assert response.headers.get("Content-Type", "").startswith("application/json"), (
            f"Wrong content type: {response.headers.get('Content-Type')}" )

    @allure.step("Check success is True")
    def check_success_true(self, response):
        data = response.json()
        assert data.get("success") is True, f"Expected success True, got {data.get('success')}"

    @allure.step("Check id list is array")
    def check_idlist_is_array(self, response):
        data = response.json()
        assert isinstance(data.get("idList"), list), "idList is not a list"
