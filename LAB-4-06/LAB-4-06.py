from machine import Pin, ADC
from time import sleep

led01 = Pin(2, Pin.OUT)
led02 = Pin(16, Pin.OUT)
led03 = Pin(17, Pin.OUT)
led04 = Pin(18, Pin.OUT)
led05 = Pin(19, Pin.OUT)
led06 = Pin(20, Pin.OUT)
led07 = Pin(21, Pin.OUT)
led08 = Pin(22, Pin.OUT)
led09 = Pin(23, Pin.OUT)
led10 = Pin(24, Pin.OUT)

switch = ADC(Pin(28))

while True:
    led01.value(False)
    led02.value(False)
    led03.value(False)
    led04.value(False)
    led05.value(False)
    led06.value(False)
    led07.value(False)
    led08.value(False)
    led09.value(False)
    led10.value(False)

    readSW = switch.read_u16()
    readSW = readSW / 65535 * 100
    sleep(5)
    print(readSW)
    if readSW > 5 and readSW <= 10:
        led01.value(True)
        print("LED 01 ON")
    elif readSW > 10 and readSW <= 20:
        led02.value(True)
        print("LED 02 ON")
    elif readSW > 20 and readSW <= 30:
        led03.value(True)
        print("LED 03 ON")
    elif readSW > 30 and readSW <= 40:
        led04.value(True)
        print("LED 04 ON")
    elif readSW > 40 and readSW <= 50:
        led05.value(True)
        print("LED 05 ON")
    elif readSW > 50 and readSW <= 60:
        led06.value(True)
        print("LED 06 ON")
    elif readSW > 60 and readSW <= 70:
        led07.value(True)
        print("LED 07 ON")
    elif readSW > 70 and readSW <= 80:
        led08.value(True)
        print("LED 08 ON")
    elif readSW > 80 and readSW <= 90:
        led09.value(True)
        print("LED 09 ON")
    elif readSW > 90 and readSW <= 100:
        led10.value(True)
        print("LED 10 ON")
