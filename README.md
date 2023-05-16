# satflasher
Using a Pi Pico W to flash it's LED depending on the elevation of a satellite.

The satellite ID in the code is [47309](https://www.n2yo.com/satellite/?s=47309) which is [CAPE-3](https://ee.louisiana.edu/research/cape/satellite-missions/cape-3) from UL Lafayette.


This code takes a Pi Pico W and checks the API at [N2YO.com](https://www.n2yo.com) to see if a satellite is overhead.

<br>
The onboard LED blink speed is based on the elevation of the satellite.

-15 to 0 degrees = 1 second flashes

1 to 15 degrees = .5 second flashes

+15 degrees = .1 second flashes

<br>
NOTE:

You will need to update the wifi.py file with your SSIDs for wireless connectivity.

You will need to replace the API key from your N2YO account to use the [API here for satellite position](https://www.n2yo.com/api/)


<a title="Michael H. („Laserlicht“), CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Raspberry_pi_pico_(cropped)_top.jpg"><img width="512" alt="Raspberry pi pico (cropped) top" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Raspberry_pi_pico_%28cropped%29_top.jpg/512px-Raspberry_pi_pico_%28cropped%29_top.jpg"></a>
