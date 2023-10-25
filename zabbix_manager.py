from zabbix_manager_configuration_policy import ZabbixManagerConfigurationPolicy
from zabbix_api import ZabbixAPI


class ZabbixManager:
    """
    Manages all servers team Zabbix operations
    """

    def __init__(self, configuration: ZabbixManagerConfigurationPolicy = None):
        self.configuration = configuration
        self.zabbix_api = ZabbixAPI(configuration.username, configuration.password, configuration.url)

if __name__ == "__main__":
    # Create a Configuration Object
    config = ZabbixManagerConfigurationPolicy()
    config.username = "Admin"
    config.password = "zabbix"
    config.url = "https://your_zabbix_api_url/api_jsonrpc.php"

    # Create a ZabbixManager Instance with the Configuration Object
    zabbix_manager = ZabbixManager(configuration=config)

    # Interact with the Zabbix API
    token = zabbix_manager.zabbix_api.get_token()
    print("Authentication Token:", token)

