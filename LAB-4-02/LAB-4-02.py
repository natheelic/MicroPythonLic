from machine import Pin
from utime import sleep

# Define an array
my_Pin = [0,14, 12, 13, 15]

for i in range(5):    
    my_Pin[i] = Pin(my_Pin[i], Pin.OUT)

def control_led(value):
    try:
        pin = int(value[0:1])
        state = value[1:2]
        if state == "1":
            my_Pin[pin].on()
            print("LED ON")
        elif state == "0":
            my_Pin[pin].off()
            print("LED OFF")
    except:
        print("Next function2")
    if value == "blink":
        for i in range(5):
            my_Pin[i].on()
            sleep(0.1)
            my_Pin[i].off()
            sleep(0.1)
    elif value == "all_on":
        for i in range(5):
            my_Pin[i].on()
    elif value == "all_off":
        for i in range(5):
            my_Pin[i].off()
    elif value == "exit":
        print("Exit")
        exit()    
    else:
        print(":(")

while True:
    _Value = input("Input LED State : ")
    control_led(_Value)
