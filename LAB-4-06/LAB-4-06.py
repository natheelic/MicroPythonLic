from machine import Pin, ADC
from time import sleep

led01 = Pin(2, Pin.OUT)
led02 = Pin(16, Pin.OUT)
led03 = Pin(17, Pin.OUT)

switch = ADC(Pin(28))

while True:
    readSW = switch.read_u16()
    readSW = readSW / 65535 * 100
    sleep(5)
    print(readSW)
    if readSW > 2500 and readSW < 3000:
        led01.value(True)
        print("LED 01 ON")
    elif readSW > 25000 and readSW < 30000:
        led02.value(True)
        print("LED 02 ON")
    elif readSW > 35000 and readSW < 40000:
        led03.value(True)
        print("LED 03 ON")
    elif readSW > 52000 and readSW < 57000:
        led01.value(False)
        led02.value(False)
        led03.value(False)
        print("ALL LED OFF")
