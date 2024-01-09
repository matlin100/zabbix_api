from zabbix_manager_configuration_policy import ZabbixManagerConfigurationPolicy


def fixture_zabbix_manager_configuration():
        zabbix_configuration = ZabbixManagerConfigurationPolicy()
        zabbix_configuration.username = "Admin"
        zabbix_configuration.password = "zabbix"
        zabbix_configuration.url = "http://192.168.108.54/zabbix/"
        return zabbix_configuration

template_Net_juniper_SNMP = {"templateid": "10231"}
cisco_Catalyst_3750v2_24FS = {"templateid": "10366"}
