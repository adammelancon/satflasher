# satflasher
Using a Pi Pico W to get the elevation of a satellite and display it on an ssd1306 display.
It also uses an 8 LED WS2812 stick to show information downloading, and changes color based on elevation.

The satellite ID in the code is [47309](https://www.n2yo.com/satellite/?s=47309) which is [CAPE-3](https://ee.louisiana.edu/research/cape/satellite-missions/cape-3) from UL Lafayette.


This code takes a Pi Pico W and checks the API at [N2YO.com](https://www.n2yo.com) to see if a satellite is overhead.

<br>
The LED colors are based on the elevation of the satellite.

-15 to 0 degrees 

1 to 15 degrees

+15 degrees

<br>
NOTE:

You will need to update the wifi.py file with your SSIDs for wireless connectivity.

You will need to replace the API key from your N2YO account to use the [API here for satellite position](https://www.n2yo.com/api/)


[Imgur](https://imgur.com/KnAct9z)
