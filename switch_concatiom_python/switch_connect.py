from netmiko import ConnectHandler
import json

juniper_success = []
cisco_success = []
failed_login = []

def juniperconnect(ip , configuration = None):
        juniper_login = {
        'device_type':  'juniper',
        'host':ip,
        'username':     'root',
        'password':     'juni108per',
        'port': 22
        }
        try:
                net_connect = ConnectHandler(**juniper_login)
                if configuration:
                        net_connect.send_config_set(configuration, exit_config_mode=False)
                juniper_success.append({"ip": ip})
                net_connect.disconnect()
                return True
        except Exception as e:
                return False

def ciscoConnect(ip, configuration = None):
        cisco_login = {
        'device_type':  'cisco_ios',
        'host': ip,
        'username':     'cisco',
        'password':     'cisco',
        'port': 22
        }
        try:
                net_connect = ConnectHandler(**cisco_login)
                if configuration:
                        try:
                                net_connect.enable()
                        except Exception as e:
                                exit(1)
                net_connect.send_config_set(configuration)
                cisco_success.append({"ip": ip})
                net_connect.disconnect()
                return True
        except Exception as e:
                return False


def add_configuration(connect, configuration):
        return connect(configuration)

def authenticate_devices(devices):
        for device in devices:
                ip_address = device['IP']
                if not juniperconnect(ip_address):
                        if not ciscoConnect(ip_address):
                                failed_login.append(device)
        with open('devicemanager/juniper_success.json','w') as json_file:
                json.dump(juniper_success,json_file,indent=4)
        with open('devicemanager/cisco_success.json','w') as json_file:
                 json.dump(cisco_success,json_file,indent=4)
        with open('devicemanager/failed_login.json','w') as json_file:
                json.dump(failed_login,json_file,indent=4)






