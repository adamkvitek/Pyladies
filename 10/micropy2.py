# micropy2.py

from machine import Pin, PWM
from time import sleep

pin_flash = Pin(0, Pin.IN)
pin_led = Pin(14, Pin.OUT)

pwm = PWM(pin_led, freq=10, duty=512)

