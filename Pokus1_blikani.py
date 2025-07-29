from machine import Pin
import time

led = Pin(25, Pin.OUT)  # Use the onboard LED on GPIO 25
while True:
    led.value(1)  # Turn on the LED
    time.sleep(1)  # Wait for 1 second
    led.value(0)  # Turn off the LED
    time.sleep(1)  # Wait for 1 second