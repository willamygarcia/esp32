from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
botao = Pin(4, Pin.IN, Pin.PULL_UP)  # Botão no pino 4

while True:
    if botao.value() == 0:  # Pressionado
        led.on()
    else:
        led.off()
    sleep(0.1)
