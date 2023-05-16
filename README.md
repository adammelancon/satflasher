# satflasher
Using a Pi Pico W to flash it's LED depending on the elevation of a satellite.

The satellite ID it's using is 47309 which is [CAPE-3](https://ee.louisiana.edu/research/cape/satellite-missions/cape-3) from UL Lafayette.


This code takes a Pi Pico W and checks the API at [N2YO.com](https://www.n2yo.com) to see if a satellite is overhead.

The onboard LED blink speed is based on the elevation of the satellite.
-15 to 0 degrees = 1 second flashes
1 to 15 degrees = .5 second flashes
> 15 degrees = .1 second flashes

You will need to replace the API key from your N2YO account to use the API here for satellite position:
https://www.n2yo.com/api/#positions
