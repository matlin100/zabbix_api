import unittest
from zabbix_manager_configuration_policy import ZabbixManagerConfigurationPolicy
from zabbix_manager import ZabbixManager

class TestZabbixManager(unittest.TestCase):
    def __init__(self):
        self.config = ZabbixManagerConfigurationPolicy()
        self.config.username = "your_username"
        self.config.password = "your_password"
        self.config.url = "https://your_zabbix_api_url/api_jsonrpc.php"
        self.zabbix_manager = ZabbixManager(configuration=self.config)

    def test_authentication(self):
        token = self.zabbix_manager.zabbix_api.get_token()
        self.assertIsNotNone(token)

    def test_add_juniper_switch_host(self):
        # Replace these values with your Juniper switch details
        payload = {
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": "juniper_switch_name",
                "interfaces": [
                    {
                        "type": 1,
                        "main": 1,
                        "useip": 1,
                        "ip": "juniper_switch_ip",
                        "dns": "",
                        "port": "10050"
                    }
                ],
                "groups": [{"groupid": "your_hostgroup_id"}],  # Replace with your actual hostgroup ID
                "templates": [{"templateid": "your_template_id"}]  # Replace with your Zabbix template ID for switches
            },
            "auth": self.zabbix_manager.zabbix_api.token,
            "id": 1
        }
        # Attempt to add the Juniper switch host
        response = self.zabbix_manager.zabbix_api.post("", json=payload)
        self.assertTrue(response.get("result").get("hostids"), "Failed to add Juniper switch host to Zabbix")

    def delete_host(self):
        delete_payload = {
            "jsonrpc": "2.0",
            "method": "host.delete",
            "params": [host_id],# get host id from the url
            "auth": self.zabbix_manager.zabbix_api.token,
            "id": 1
          }
        delete_response = self.zabbix_manager.zabbix_api.post("", json=delete_payload)
        self.assertTrue(delete_response.get("result").get("hostids"), "Failed to delete Juniper switch host from Zabbix")

    def get_info(self):
          # Get data for the Juniper switch host
        host_data = self.zabbix_manager.zabbix_api.get(f"/host/{host_id}")
        self.assertIsNotNone(host_data, "Failed to retrieve data for Juniper switch host from Zabbix API")


if __name__ == "__main__":
    unittest.main()
