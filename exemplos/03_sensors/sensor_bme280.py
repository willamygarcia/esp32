from machine import I2C, Pin
from time import sleep
import bme280

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = bme280.BME280(i2c=i2c)

while True:
    temp, press, hum = sensor.read_compensated_data()
    print("Temperatura: {:.2f} °C".format(temp / 100))
    print("Pressão: {:.2f} hPa".format(press / 25600))
    print("Umidade: {:.2f} %".format(hum / 1024))
    sleep(2)
