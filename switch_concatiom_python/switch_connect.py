from netmiko import ConnectHandler, NetMikoTimeoutException
from configurations.switch_connection_configurtion import cisco_login, juniper_login
import time

juniper_success = []
cisco_success = []
failed_login = []

def juniperconnect(ip ):
        login = juniper_login(ip)
        try:
                net_connect = ConnectHandler(**login)
                juniper_success.append({"ip": ip})
                net_connect.disconnect()
                return True
        except Exception as e:
                return False
def ciscoConnect(ip):
        login = cisco_login(ip)
        try:
                net_connect = ConnectHandler(**login)
                cisco_success.append({"ip": ip})
                net_connect.disconnect()
                return True
        except Exception as e:
                return False

def ciscoConfig(ip,config_set):
        login = cisco_login(ip)
        try:
                net_connect = ConnectHandler(**login)
                try:
                        net_connect.enable()
                except Exception as e:
                        print(e)
                net_connect.send_config_set(config_set)
                net_connect.save_config()
                net_connect.disconnect()

        except Exception as e:
                print("Failed to connect to the device: ", str(e))
                net_connect.disconnect()
        return True
def juniperConfig(ip,config_set):
        login = juniper_login(ip)
        try:
                net_connect = ConnectHandler(**login)

                for command in config_set:
                        net_connect.send_config_set(command)
                        time.sleep(5)
                net_connect.commit()
                net_connect.disconnect()
                print(f'commit in {ip}')
                return True
        except NetMikoTimeoutException as e:
                print(f'NetMiko Timeout error for device {ip}: {str(e)}')
        except Exception as e:
                print("Failed to connect to the device: ", str(e))
                net_connect.disconnect()
                exit(1)

def authenticate_devices(devices):
        for device in devices:
                ip_address = device['IP']
                if not juniperconnect(ip_address):
                        if not ciscoConnect(ip_address):
                                failed_login.append(device)
        # with open('devicemanager/juniper_success.py', 'w') as json_file:
        #         json.dump(juniper_success,json_file,indent=4)
        # with open('devicemanager/cisco_success.py', 'w') as json_file:
        #          json.dump(cisco_success,json_file,indent=4)
        # with open('devicemanager/failed_login.py', 'w') as json_file:
        #         json.dump(failed_login,json_file,indent=4)





