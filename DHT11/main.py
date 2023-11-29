import time
from machine import Pin
import dht

sensor = dht.DHT11(Pin(15))
led01 = Pin(10, Pin.OUT)
led02 = Pin(11, Pin.OUT)
led03 = Pin(12, Pin.OUT)

print("TEST PI PICO DHT11 Controll LED ")
while True:
    try:
        sensor.measure()
        print(sensor.temperature())
        print(sensor.humidity())
        if sensor.temperature() > 32:
            led01.value(1)
            led02.value(1)
            led03.value(1)
        elif sensor.temperature() <= 31 & sensor.temperature() <= 32:
            led01.value(1)
            led02.value(1)
            led03.value(0)
        elif sensor.temperature() >= 29 & sensor.temperature() <= 30:
            led01.value(1)
            led02.value(0)
            led03.value(0)
        elif sensor.temperature() <= 28:
            led01.value(0)
            led02.value(0)
            led03.value(0)
    except OSError as e:
        print("Failed to read sensor.!")
    time.sleep(1)
