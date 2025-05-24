import dht
from machine import Pin
from time import sleep

sensor = dht.DHT22(Pin(15))  # Conectado ao pino 15

while True:
    sensor.measure()
    print("Temperatura:", sensor.temperature(), "°C")
    print("Umidade:", sensor.humidity(), "%")
    sleep(2)
