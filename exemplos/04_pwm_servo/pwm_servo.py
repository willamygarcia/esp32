from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(13), freq=50)

def mover(angulo):
    duty = int((angulo / 180) * 102 + 26)  # Aproximação para SG90
    servo.duty(duty)

while True:
    mover(0)
    sleep(1)
    mover(90)
    sleep(1)
    mover(180)
    sleep(1)
