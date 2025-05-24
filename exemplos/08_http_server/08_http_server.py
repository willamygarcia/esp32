import socket
import network

# Conecte-se ao Wi-Fi primeiro

html = """<!DOCTYPE html>
<html>
  <head><title>ESP32</title></head>
  <body><h1>Olá, mundo!</h1></body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)
print("Servidor em http://", addr)

while True:
    conn, addr = s.accept()
    print("Cliente conectado:", addr)
    conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
    conn.send(html)
    conn.close()
