from machine import Pin, time_pulse_us
from time import sleep

trigger = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)

def medir_distancia():
    trigger.off()
    sleep(0.01)
    trigger.on()
    sleep(0.00001)
    trigger.off()

    duracao = time_pulse_us(echo, 1)
    distancia = duracao / 58.0  # cm
    return distancia

while True:
    dist = medir_distancia()
    print("Distância:", dist, "cm")
    sleep(1)
