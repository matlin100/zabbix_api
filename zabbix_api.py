import requests
import json


class ZabbixAPI:
    """
    API for all zabbix operations.
    """
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        self.token = self.get_token()

    def get_token(self):
        """
        Get authentication token from the Zabbix API.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.username,
                "password": self.password
            },
            "id": 1
        }

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = self.post("", json=payload)  # Sending POST request to obtain token
        token = response.get("result")
        if token is None:
            raise RuntimeError("Failed to obtain authentication token from Zabbix API.")
        return token

    def get(self, request_path, params=None, headers=None):
        """
        Execute a GET request to the specified API path.

        Parameters:
            request_path (str): The API path to request.
            params: URL parameters to include in the request.
            headers: Headers to include in the request.
        Returns:
            response(json): requests response.
        """
        response = requests.get(f"{self.url}{request_path}", headers=self.headers, params=params, timeout=120)
        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"Request to Delinea api returned an error {response.status_code}, the response is:\n{response.text}"
            )
        return response.json()

    def post(self, request_path, json=None, data=None, headers=None):
        """
        Execute a POST request to the specified API path.

        Parameters:
            request_path(str): api path.
            json (json): The request data as a JSON object.
            data: Data to send in the request body.
            headers: Headers to include in the request.
        Returns:
            response(json): requests response.
        """
        response = requests.post(f"{self.url}{request_path}", headers=self.headers, json=json, data=data, timeout=120)
        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"Request to Delinea api returned an error {response.status_code}, the response is:\n{response.text}"
            )
        return response.json()

    def put(self, request_path, json=None, data=None, headers=None):
        """
        Execute a PUT request to the specified API path.

        Parameters:
            request_path(str): api path.
            json (json): The request data as a JSON object.
            data: Data to send in the request body.
            headers: Headers to include in the request.
        Returns:
            response(json): requests response.
        """
        response = requests.put(f"{self.url}{request_path}", headers=self.headers, json=json, data=data, timeout=120)
        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"Request to Delinea api returned an error {response.status_code}, the response is:\n{response.text}"
            )
        return response.json()

    def delete(self, request_path, headers=None):
        """
        Execute a DELETE request to the specified API path.

        parameters:
            request_path(str): api path.
            json (json): The request data as a JSON object.
            data: Data to send in the request body.
            headers: Headers to include in the request.
        Returns:
            response(json): requests response.
        """
        response = requests.delete(f"{self.url}{request_path}", headers=self.headers, timeout=120)
        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"Request to Delinea api returned an error {response.status_code}, the response is:\n{response.text}"
            )
        return response.json()
