from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)  # Pino do LED interno

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
