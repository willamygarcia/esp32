from machine import Pin, I2C
import ssd1306
from time import sleep

i2c = I2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("Hello ESP32!", 0, 0)
oled.text("com MicroPython", 0, 10)
oled.show()
