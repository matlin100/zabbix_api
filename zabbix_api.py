import requests
import json


class ZabbixAPI:
    """
    API for all zabbix operations
    """

    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        self.headers = {"Content-Type": "application/json"}
        self.token = self.get_token()


    def get_token(self):
        """
        get authentication token from Zabbix API
        """
        body = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.username,
                "password": self.password
            },
            "id": 1
        }
        response = self.post(request_path="api_jsonrpc.php", json=body, headers=self.headers)
        if not response:
            raise RuntimeError("failde to get token from the api.")
        return json.loads(response.text)["result"]

    def get(self, request_path, params=None, headers=None, json=None):
        """
        Ececute a get request to the API path
        parameters:
            request_path(str): the API path to request.
            params: URL for the request
            headers: Headers to include in the request
        returns:
        response(json)
        """
        response = requests.get(f"{self.url}{request_path}", headers=headers, params=params, json=json, timeout=120)
        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"error status code : {response.status_code} the error is : {response.text}"
            )
        return response.json()

    def post(self, request_path=None, json=None, data=None, headers=None):
        """
        Ececute a get request to the API path
        parameters:
            request_path(str): the API path to request.
            json: the request data in json object
            data : data to send to the request body
            headers: Headers to include in the request
        returns:
        response(json)
        """
        response = requests.post(f"{self.url}{request_path}", headers=headers, json=json, data=data, timeout=120)
        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"error status code : {response.status_code} the error is : {response.text}"

            )
        return response

    def put(self, request_path, json=None, data=None, headers=None, params=None):
        """
        Ececute a get request to the API path
        parameters:
            request_path(str): the API path to request.
            json: the request data in json object
            data : data to send to the request body
            headers: Headers to include in the request
        returns:
        response(json)
        """
        response = requests.put(f"{self.url}{request_path}", headers=headers, json=json, data=data, params=params,
                                timeoit=120)
        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"error status code : {response.status_code} the error is : {response.text}"
            )
        return response.json()

    def delete(self, request_path, headers=None):
        """
        Ececute a get request to the API path
        parameters:
            request_path(str): the API path to request.
            json: the request data in json object
            data : data to send to the request body
            headers: Headers to include in the request
        returns:
        response(json)
        """
        response = requests.delete(f"{self.url}{request_path}", headers=headers, timeoit=120)
        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"error status code : {response.status_code} the error is : {response.text}"
            )
        return response.json()
