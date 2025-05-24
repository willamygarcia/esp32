from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(34))  # Pino ADC (entrada analógica)
adc.atten(ADC.ATTN_11DB)  # Faixa de 0-3.3V

while True:
    valor = adc.read()
    tensao = valor * 3.3 / 4095
    temperatura = tensao * 100  # LM35: 10mV por °C
    print("Temperatura (°C):", temperatura)
    sleep(2)
