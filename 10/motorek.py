from machine import Pin, PWM
from time import sleep

pin_motorku = Pin(2, Pin.OUT)
pwm = PWM(pin_motorku, freq=50, duty=30)
pwm.duty(35)
