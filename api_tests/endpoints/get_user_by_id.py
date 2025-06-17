import allure
from .base_endpoint import BaseEndpoint

class GetUserByIdEndpoint(BaseEndpoint):
    ENDPOINT = "user"

    @allure.step("Send GET /user/{user_id}")
    def send_request(self, user_id, method="GET"):
        path = f"{self.ENDPOINT}/{user_id}"
        return super().send_request(method, path)
