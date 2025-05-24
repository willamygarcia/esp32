from machine import Pin
from time import sleep

pir = Pin(27, Pin.IN)

while True:
    if pir.value():
        print("Movimento detectado!")
    else:
        print("Sem movimento.")
    sleep(1)
