import network
import time
from config_secrets import *

# Wi-Fi configuration
ssid_list = ['mwifi', 'PublicLibrary']  # List of Wi-Fi SSIDs to try
# List of passwords for each Wi-Fi SSID in secrets_config.py

# Wireless ########################################
def connect_to_wifi(ssid, password):
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
    for i in range(len(ssid_list)):
        ssid = ssid_list[i]
        password = password_list[i]
        if connect_to_wifi(ssid, password):
            return True
    return False
# Wireless ########################################