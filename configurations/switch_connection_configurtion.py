
def cisco_login(ip):
    cisco_login = {
        'device_type':  'cisco_ios',
        'host': ip,
        'username':     'cisco',
        'password':     'cisco',
        'secret':       'cisco',
        'port': 22
        }
    return cisco_login

def juniper_login(ip):
    juniper_login = {
        'device_type':  'juniper',
        'host': ip,
        'username':     'root',
        'password':     'juni108per',
        'port': 22
        }
    return juniper_login


def enable_juniper_snmp_config(ip):
    enable_juniper_snmp_config = ['set snmp community zabbix_api authorization read-only',
                                 'set snmp community zabbix_api clients  192.168.108.180',
                                 ]
    return enable_juniper_snmp_config
enable_cisco_snmp_config = ['snmp-server community zabbix_api RO',
                            'snmp-server host 192.168.108.180 version 2c zabbix_api']
