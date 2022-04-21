from requests import request
from urllib.parse import urljoin

class Session:
    # TODO Add support for async requests
    # TODO Write better exception messages
    
    def __init__(self, base_url: str):
        self.base_url = base_url

    def auth_status(self):
        endpoint = urljoin(self.base_url, "iserver/auth/status")
        response = request(
            "POST",
            endpoint,
            verify=False,
        )
        status_code = response.status_code
        if not response.ok:
            raise Exception(f"Session authentication error - code: {status_code}")
        response_data = response.json()
        if response_data["authenticated"] is False:
            raise Exception(f"User session is not authenticated - code: {status_code} - data: {response_data}")
        elif response_data["competing"] is True:
            raise Exception(f"User session is competing - code: {status_code} data: {response_data}")
        return response_data

    def keep_alive(self):
        endpoint = urljoin(self.base_url, "sso/validate")
        request(
            "GET",
            endpoint,
            verify=False,
        )

    def reauthenticate(self):
        endpoint = urljoin(self.base_url, "iserver/reauthenticate")
        request(
            "POST",
            endpoint,
            verify=False,
        )