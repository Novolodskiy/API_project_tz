import allure
from .base_endpoint import BaseEndpoint

class GetUsersEndpoint(BaseEndpoint):
    ENDPOINT = "users"

    @allure.step("Send GET /users")
    def send_request(self, gender=None, method="GET"):
        params = {"gender": gender} if gender is not None else None
        return super().send_request(method, self.ENDPOINT, params=params)
