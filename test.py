import unittest
from zabbix_manager_configuration_policy import ZabbixManagerConfigurationPolicy
from zabbix_manager import ZabbixManager


class TestZabbixManager(unittest.TestCase):

    def test_authentication(self):
        config = ZabbixManagerConfigurationPolicy()
        config.username = "your_username"
        config.password = "your_password"
        config.url = "https://your_zabbix_api_url/api_jsonrpc.php"
        zabbix_manager = ZabbixManager(configuration=config)
        token = zabbix_manager.zabbix_api.get_token()
        self.assertIsNotNone(token)



if __name__ == "__main__":
    unittest.main()


