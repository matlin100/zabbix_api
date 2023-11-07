from zabbix_manager_configuration_policy import ZabbixManagerConfigurationPolicy


def fixture_zabbix_configuration():
        zabbix_configuration = ZabbixManagerConfigurationPolicy()
        zabbix_configuration.username = "Admin"
        zabbix_configuration.password = "zabbix"
        zabbix_configuration.url = "http://192.168.108.180/zabbix/"
        return zabbix_configuration

snmp_config = 'set snmp community zabbix_api authorization read-only'
