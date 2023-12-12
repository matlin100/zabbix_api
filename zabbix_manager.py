import json
from zabbix_manager_configuration_policy import ZabbixManagerConfigurationPolicy
from zabbix_api import ZabbixAPI
from configurations.payload import payload_host_get_params
class ZabbixManager:
    """
    Manages all server from operation
    """
    def __init__(self, configuration: ZabbixManagerConfigurationPolicy = None):
        self.configuration = configuration
        self.zabbix_api = ZabbixAPI(configuration.username, configuration.password, configuration.url)
        self.headers = self.zabbix_api.headers
        self.payload = {
            "jsonrpc": "2.0",
            "method": "",
            "auth": self.zabbix_api.token,
            "id": 4
        }

    def get_host(self, hostName):
        self.payload["method"] = "host.get"
        self.payload["params"] = payload_host_get_params
        self.payload["params"]["filter"] = {"host": hostName}
        print(self.payload)
        host_data = self.zabbix_api.post(request_path="api_jsonrpc.php", headers=self.headers, json=self.payload)
        print(json.loads(host_data.text))
        return json.loads(host_data.text)

    def create_host(self, hostName, ip, template_ids):
        self.payload["method"] = "host.create"
        self.payload["params"] = {
            "host": hostName,
            "interfaces": [
                    {
                        "type": 1,
                        "main": 1,
                        "useip": 1,
                        "ip": ip,
                        "dns": "",
                        "port": "10050"
                    }
                ],
                "groups": [{"groupid": "9"}],
                "templates":template_ids,
            }
        host_data = self.zabbix_api.post(request_path="api_jsonrpc.php", headers=self.headers, json=self.payload)
        print(json.loads(host_data.text))
        return json.loads(host_data.text)

    def update_host(self, hostID):
        self.payload["method"] = "host.update"
        self.payload["params"] = {"hostid": hostID}
        host_data = self.zabbix_api.post(request_path="api_jsonrpc.php", headers=self.headers, json=self.payload)
        print(json.loads(host_data.text))
        return json.loads(host_data.text)

    def delete_host(self, hostID):
        self.payload["method"] = "host.update"
        self.payload["params"] = [hostID],
        host_data = self.zabbix_api.post(request_path="api_jsonrpc.php", headers=self.headers, json=self.payload)
        print(json.loads(host_data.text))
        return json.loads(host_data.text)

    def provision_host(self, hostName, ip, hostID):
        host = self.get_host(hostName)
        if host:
            self.update_host(hostID)
        else:
            self.create_host(hostName, ip)
