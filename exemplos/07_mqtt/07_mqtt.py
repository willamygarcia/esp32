import network
import time
from umqtt.simple import MQTTClient

# Conecte-se ao Wi-Fi (veja exemplo 06)
# Após conexão:

client = MQTTClient("esp32", "broker.hivemq.com")
client.connect()

while True:
    client.publish(b"curso/esp32", b"Hello MQTT")
    print("Mensagem publicada!")
    time.sleep(5)
