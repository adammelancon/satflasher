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

led = Pin("LED", Pin.OUT)
led.off()

neopin = machine.Pin(2, Pin.OUT)
num_pixels = 8  # Number of Neopixels in the strip
np = neopixel.NeoPixel(neopin, num_pixels, bpp=3, timing=1)
np[0] = (2,0,0)
np.write()

sleep_timer = 30  # Time to wait between API calls when under the horizon.
live_timer = 5
sat_name = "CAPE-3"
sat_id = 47309    # SET TO CAPE-3 47309   
lat = 30.20128
long = -92.04119
elev_in_m = 10



def get_satellite_coordinates(satid, la, lo, elev):
    # API information
    api_key = "xxx-xxx-xxx-xxx"
    url = f"https://api.n2yo.com/rest/v1/satellite/positions/{satid}/{la}/{lo}/{elev}/1&apiKey={api_key}"
    
    try:
        print("Connecting to N2YO API...")
        response = urequests.get(url)
#         for _ in range(3):
#             led.on()
#             time.sleep(0.1)
#             led.off()
#             time.sleep(0.1)
        if response.status_code == 200:
            print("Getting updates...")
            Label(elevwri, 45, 0, f'-Elev: updating')
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



def blink(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
#         led.toggle()
#         np[0] = (5,2,5)
        np.write()
        time.sleep(interval)
#     led.off()
    clear_np()



async def check_elevation():
    while True:
        elevation = get_satellite_coordinates(sat_id, lat, long, elev_in_m)
        
        if elevation is not None:
            refresh(ssd, True)
            Label(titlewri, 1, 20, 'Tracking:', invert=True)
            Label(satwri, 26, 0, sat_name)
            refresh(ssd)
            # Clear previous text
            Label(elevwri, 45, 0, '-Elev: ')
            refresh(ssd)
            # Set new elevation value
            Label(elevwri, 45, 0, f'-Elev: {elevation} deg')
            
            refresh(ssd)
            clear_np()
            
            if elevation <= -15:
                led.off()
                print("sleep timer < -15")
                await asyncio.sleep(sleep_timer)  # Check according to sleep_timer
                
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

