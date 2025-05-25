from machine import ADC, Pin
from time import sleep

mq2 = ADC(Pin(32))
mq2.atten(ADC.ATTN_11DB)

while True:
    valor = mq2.read()
    print("Leitura MQ-2 (fumaça/gás):", valor)
    sleep(1)
