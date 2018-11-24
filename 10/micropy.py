# micropy.py

from machine import Pin
from time import sleep

pin_flash = Pin(0, Pin.IN)
pin_led = Pin(14, Pin.OUT)

while True:
#    pin_led.value(pin_flash.value())
#    sleep(1)
    pin_led.value(1)
    sleep(1/1000)
    pin_led.value(0)
    sleep(3/3000)

# linux držet ctrl a zmáčkni a q 
# ampy -p /dev/ttyUSB0 run micropy.py

