import urequests
import time

API_KEY = "SUA_CHAVE"
URL = "https://api.thingspeak.com/update?api_key=" + API_KEY

valor = 25  # Exemplo fixo

while True:
    r = urequests.get(URL + "&field1=" + str(valor))
    print("Enviado para ThingSpeak:", r.text)
    r.close()
    time.sleep(15)
