from machine import Pin
import time

led = Pin(25, Pin.OUT)  # Onboard LED na GPIO 25

for i in range(10):     # Zabliká 10x
    led.value(1)        # LED zapni
    time.sleep(0.5)
    led.value(0)        # LED vypni
    time.sleep(0.5)
