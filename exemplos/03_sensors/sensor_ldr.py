from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)

while True:
    valor = adc.read()
    print("Luz ambiente (valor ADC):", valor)
    sleep(1)
