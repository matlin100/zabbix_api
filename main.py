from tests.test_integration import *
from configurations.switch_connection_configurtion import enable_cisco_snmp_config, enable_juniper_snmp_config
from configurations.devicemanager.juniper_success import juniper_switch_list
from configurations.devicemanager.cisco_success import cisco_switch_list
from configurations.fixture_zabbix_manager_configuration import template_Net_juniper_SNMP, cisco_Catalyst_3750v2_24FS

def enable_SNMP_to_juniper_switched(juniper_ip_list):
    for switch in juniper_ip_list:
        if not test_config_SNMP_juniper_switch(ip=switch['ip'], configuration=enable_juniper_snmp_config(switch['ip'])):
            return False
    return True

def enable_SNMP_to_cisco_switched(cisco_ip_list):
    for switch in cisco_ip_list:
        if not test_config_SNMP_Cisci_switch(ip=switch['ip'], configuration=enable_cisco_snmp_config):
            return False
    return True
    return True

def create_zabbixHost_to_all_switched(ip_list , swithc_company_name, template_id):
    for switch in ip_list:
        ip = switch['ip']
        octats = ip.split('.')
        last_octate = octats[-1]
        detals = test_create_host(host_name=f'{swithc_company_name} ip  {last_octate}', ip=ip, template_id=template_id)
        print(detals)


if __name__ == '__main__':
 #    create_zabbixHost_to_all_switched(juniper_switch_list, 'juniper', template_Net_juniper_SNMP)
 #    create_zabbixHost_to_all_switched(cisco_switch_list, 'cisco', cisco_Catalyst_3750v2_24FS)
    
    stest_get_host('juniper ip 19')
