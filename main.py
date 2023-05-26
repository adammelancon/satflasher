import urequests
import json
import time
import uasyncio as asyncio
from machine import Pin
import machine
import neopixel
from wifi import *
from synctime import *
from satdisplay import *
from config_secrets import *

# Onboard LED setup for Pi Pico
led = Pin("LED", Pin.OUT)
led.off()

# WS2812 (Neopixel) setup
neopin = machine.Pin(2, Pin.OUT)
num_pixels = 8  # Number of Neopixels in the strip
np = neopixel.NeoPixel(neopin, num_pixels, bpp=3, timing=1)
# Clear pixels on startup
np[0] = (2,0,0)  
np.write()

sleep_timer = 90  # Time to wait between API calls when under the horizon.
live_timer = 10   # Time to wait between API calls when over the horizon.
# sat_name = "CAPE-3"
# sat_id = 47309    # SET TO CAPE-3 47309
sat_name = "ISS"
sat_id = 25544     # SET TO ISS 25544   
lat = 30.20128     # Your Lat
long = -92.04119   # Your Long
elev_in_m = 10     # Your Elevation in M



def get_satellite_coordinates(satid, la, lo, elev):
    '''Connects to n2yo and gets json of satellite data.  Returns elevation.'''
    # api_key is hidden in config_secrets.py
    url = f"https://api.n2yo.com/rest/v1/satellite/positions/{satid}/{la}/{lo}/{elev}/1&apiKey={api_key}"
    
    try:
        print("Connecting to N2YO API...")
        response = urequests.get(url)
        
        if response.status_code == 200:
            print("Getting updates...")
            refresh(ssd, True)
            Label(elevwri, 45, 0, 'Elev: updating')
            refresh(ssd)
            
            for i in range(3):
                for index in reversed(range(8)):
                    np[index] = (0,2,0)
                    np.write()
                    time.sleep(.10)
                    clear_np()

            try:
                data = response.json()
                elevation = data["positions"][0]["elevation"]
                print(f"{sat_name}'s elevation is {elevation} degrees.")
                
                    
                return elevation
            except ValueError:
                print("Failed to parse JSON response.")
                for index in range(8):
                    np[index] = (2,0,0)
                    np.write()
                    time.sleep(.25)
        else:
            print("Failed to retrieve satellite coordinates.")
            for index in range(8):
                np[index] = (2,0,0)
                np.write()
                time.sleep(.25)
            
    except Exception as e:
        print("An error occurred during the API request:", e)

    return None


async def check_elevation():
    ''' Checks for satellite elevation and updates screen and leds based on result'''
    
    prev_elevation = 0
    while True:
        elevation = get_satellite_coordinates(sat_id, lat, long, elev_in_m)
        
        if elevation is not None:
            refresh(ssd, True)
            Label(titlewri, 1, 20, 'Tracking:', invert=True)
            if prev_elevation == 0:
                Label(satwri, 26, 0, sat_name)
                refresh(ssd)
            elif elevation > prev_elevation:
                Label(satwri, 26, 0, sat_name + " - Asc.")
                refresh(ssd)
            elif elevation < prev_elevation:
                Label(satwri, 26, 0, sat_name + " - Desc.")
                refresh(ssd)

            # Clear previous text
            Label(elevwri, 45, 0, 'Elev: ')
            refresh(ssd)
            # Set new elevation value
            Label(elevwri, 45, 0, f'Elev: {elevation} deg')
            
            refresh(ssd)
            clear_np()
            prev_elevation = elevation
            
            if elevation <= -15:
                print("sleep timer < -15")
                await asyncio.sleep(sleep_timer)
                
            elif -15 <= elevation <= 0:
                np.fill((1,0,0))
                np.write()
                print("live timer -15 - 0")
                await asyncio.sleep(live_timer)
                
            elif 1 <= elevation <= 15:
                np.fill((0,0,5))
                np.write()
                print("live timer 1 - 15")
                await asyncio.sleep(live_timer)
                
            elif elevation > 15:
                np.fill((0,3,0))
                np.write()
                print("live timer > 15")
                await asyncio.sleep(live_timer)
                

def clear_np():
    ''' simple function to clear ws2812 leds (neopixels)'''
    np.fill((0, 0, 0))
    np.write()
    
    
# Run program if connected to Wi-Fi network
if connect_to_wifi_networks():
    Label(satwri, 26, 0, "SAT TRACKER")
    refresh(ssd)
    clear_np()
    loop = asyncio.get_event_loop()
    loop.create_task(check_elevation())
    loop.run_forever()
else:
    print('No Wi-Fi networks available')

