import network
import urequests
import time
from machine import Pin

led = Pin(2, Pin.OUT)
x = 1

BLYNK_AUTH = "TOKEN"
BLYNK_URL = "http://blynk.cloud/external/api/update"

# --- Wi-Fi ---
SSID = ""
PASSWORD = ""

def piscarMaisRapido():
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
  
def piscarMaisLento():
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Conectando-se ao Wi-Fi...", end="")
    while not wlan.isconnected():

        print(".", end="")
        time.sleep(1)
    print("\nWi-Fi conectado! IP:", wlan.ifconfig()[0])

def send_to_blynk(qtd):
    try:
        qtdPiscadas_url = f"{BLYNK_URL}?token={BLYNK_AUTH}&V0={qtd}"
        urequests.get(qtdPiscadas_url)
        print(f"Enviado para Blynk - Quantidade de Piscadas: {qtd}")
    except Exception as e:
        print("Erro ao enviar dados para Blynk:", e)

def main(x):
    connect_wifi()
    while True:
        if (x % 2 == 0):
            piscarMaisRapido()
            print('Valor de X é par  X = ' , x)
        else:
            piscarMaisLento()
            print('Valor de X é impar  X = ' , x)
     
        x=x+1
        send_to_blynk(x)
        time.sleep(10)

main(x)
