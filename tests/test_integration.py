from zabbix_manager import ZabbixManager
from conftest import fixture_zabbix_configuration
from switch_concatiom_python.switch_connect import juniperconnect, ciscoConnect

def test_get_host():
    zabbix_manager = ZabbixManager(fixture_zabbix_configuration())
    host_get = zabbix_manager.get_host("juniper_switch_name")

def test_create_host():
    zabbix_manager = ZabbixManager(fixture_zabbix_configuration())
    host_create = zabbix_manager.create_host("juniper_switch_name", "192.168.199.100")

def test_update_host():
    zabbix_manager = ZabbixManager(fixture_zabbix_configuration())
    host_update = zabbix_manager.update_host("10445")

def test_delete_host():
    zabbix_manager = ZabbixManager(fixture_zabbix_configuration())
    host_delete = zabbix_manager.delete_host("10445")

def test_provision_host():
    zabbix_manager = ZabbixManager(fixture_zabbix_configuration())
    host_provision = zabbix_manager.provision_host("juniper_switch_name", "192.168.199.100", "10445")

def test_connect_juniper_switch():
    connected = juniperconnect(ip='192.168.199.2')
    return connected

def test_connect_cisco_switch():
    connected = ciscoConnect(ip='192.168.199.2')
    return connected

def test_config_SNMP_juniper_switch():
    connected = juniperconnect(ip='192.168.199.100', configuration='set snmp community zabbix_api authorization read-only')
    return connected

def test_config_SNMP_Cisci_switch():
    connected = juniperconnect(ip='192.168.199.100', configuration='snmp-server community zabbix_api RO')
    return connected

print(test_config_SNMP_juniper_switch())
print(test_config_SNMP_Cisci_switch())

