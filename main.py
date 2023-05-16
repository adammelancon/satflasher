import urequests
import json
import time
from machine import Pin
from wifi import *
from synctime import *

led = Pin("LED", Pin.OUT)
led.off()

api_timer = 60  # Time to wait between API calls when under the horizon.
blink_length = 20 

def get_satellite_coordinates():
    # API information
    sat_id = 47309   # SET TO CAPE-3 47309   
    lat = 30.20128
    long = -92.04119
    elev_in_m = 10
    api_key = "XXXXXX-XXXXXX-XXXXXX-XXXX"
    url = f"https://api.n2yo.com/rest/v1/satellite/positions/{sat_id}/{lat}/{long}/{elev_in_m}/1&apiKey={api_key}"
    
    try:
        print("Connecting to N2YO API...")
        response = urequests.get(url)
        for _ in range(3):
            led.on()
            time.sleep(0.1)
            led.off()
            time.sleep(0.1)
        if response.status_code == 200:
            print("Getting updates...")
            try:
                data = response.json()
                elevation = data["positions"][0]["elevation"]
                print(f"Satellite {sat_id}'s elevation is {elevation} degrees.")
                return elevation
            except ValueError:
                print("Failed to parse JSON response.")
        else:
            print("Failed to retrieve satellite coordinates.")
    except Exception as e:
        print("An error occurred during the API request:", e)

    return None

def blink(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        led.toggle()
        time.sleep(interval)
    led.off()

# Run program if connected to Wi-Fi network
if connect_to_wifi_networks():
    elevation = get_satellite_coordinates()
    
    while True:
        if elevation is not None:
            if elevation <= -15:
                led.off()
                time.sleep(api_timer)  # Check according to API timer.
            elif -15 <= elevation <= 0:
                blink(1, blink_length)  # Blink once per second for 10 seconds
            elif 1 <= elevation <= 15:
                blink(0.5, blink_length)  # Blink every 0.5 seconds for 10 seconds
            elif elevation > 15:
                blink(0.1, blink_length)  # Blink every 0.1 seconds for 10 seconds
        
        time.sleep(1)  # Delay for 1 second before the next check
        elevation = get_satellite_coordinates()  # Update elevation for further checks

else:
    print('No Wi-Fi networks available')

