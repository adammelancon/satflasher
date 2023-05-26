import network
import time
from config_secrets import *

ssid_list = ['mwifi', 'PublicLibrary']  # List of Wi-Fi SSIDs to try
# List of passwords for each Wi-Fi SSID in secrets_config.py


def connect_to_wifi(ssid, password):
    ''' takes an ssid/password combo and attempts to connect to wireless'''
    
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    print(f'Attempting connection to "{ssid}"...')
    
    for _ in range(10):  # Try to connect for 10 seconds
        if station.isconnected():
            print(f"Connected to {ssid}.")
            print("")
            return True
        time.sleep(1)
        
    else:
        print('Failed to connect to', ssid)
        station.disconnect()
        station.active(False)
        return False


def connect_to_wifi_networks():
    ''' Loops through a list of ssid/password combos and passes it off to connect.
        This allows me to have multiple ssid/passwords in my script'''
    
    for i in range(len(ssid_list)):
        ssid = ssid_list[i]
        password = password_list[i]
        if connect_to_wifi(ssid, password):
            return True
        
    return False