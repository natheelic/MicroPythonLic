from machine import Pin
from utime import sleep

numbers = [14, 12, 13, 15]


# Define each number as an output pin
output_pins = []
for number in numbers:
    output_pins.append(Pin(number, Pin.OUT))

def control_led(mode):
    if mode == 1:
        for output_pin in output_pins:
            output_pin.on()
            sleep(0.1)
            output_pin.off()
            sleep(0.1)
    elif mode == 2:
        for output_pin in output_pins:
            output_pin.on()
        sleep(1)
        for output_pin in output_pins:
            output_pin.off()
        sleep(1)
    elif mode == 3:
        for output_pin in output_pins:
            output_pin.on()
    elif mode == 4:
        for output_pin in output_pins:
            output_pin.off()            
while True:
    for rn in range(1,4):
        control_led(rn)