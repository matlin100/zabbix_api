from zabbix_manager import ZabbixManager
from configurations.fixture_zabbix_manager_configuration import fixture_zabbix_manager_configuration
from switch_concatiom_python.switch_connect import *


def get_host(host_name):
    zabbix_manager = ZabbixManager(fixture_zabbix_manager_configuration())
    host_get = zabbix_manager.get_host(hostName=host_name)
    return host_get
def create_host(host_name, ip,template_id = None):
    zabbix_manager = ZabbixManager(fixture_zabbix_manager_configuration())
    host_create = zabbix_manager.create_host(hostName=host_name, ip=ip, template_id=template_id)
    return host_create
def update_host():
    zabbix_manager = ZabbixManager(fixture_zabbix_manager_configuration())
    host_update = zabbix_manager.update_host("10445")
    return host_update
def delete_host():
    zabbix_manager = ZabbixManager(fixture_zabbix_manager_configuration())
    host_delete = zabbix_manager.delete_host("10445")
    return host_delete

def connect_juniper_switch(ip):
    connected = juniperconnect(ip)
    return connected

def connect_cisco_switch(ip):
    connected = ciscoConnect(ip)
    return connected

def config_SNMP_juniper_switch(ip, configuration):
    connected = juniperConfig(ip, configuration)
    return connected

def config_SNMP_Cisci_switch(ip, configuration):
    connected = ciscoConfig(ip, configuration)
    return connected


