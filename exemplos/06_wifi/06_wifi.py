import network
import time

ssid = 'SUA_REDE'
senha = 'SUA_SENHA'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, senha)

print("Conectando...")
while not wifi.isconnected():
    time.sleep(1)

print("Conectado com IP:", wifi.ifconfig()[0])
