# GND pásku (bílý drátek) -- jiný drát --GND
# DI (data in - zelený drátek) -- jíný drát --  D4
# +5V (červený drátek) -- jiný drát -- 3V3
# spustit picocom -b 115200 --flow n /dev/ttyUSB0

from machine import Pin
from neopixel import NeoPixel

POCET_LED = 8
pin = Pin(2, Pin.OUT)
np = NeoPixel(pin, POCET_LED)
np[0] = (10, 10, 10)
np[1] = (10, 0, 0)
np[2] = (100, 0, 100)
np[3] = (0, 10, 0)
np[4] = (115, 138, 10)
np[5] = (50, 0, 50)
np[6] = (10, 40, 10)
np[7] = (20, 60, 70)
np.write() # Zobrazení barev

