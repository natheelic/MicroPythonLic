from tkinter import BUTT
import machine
import utime
import dht
import sys
from machine import Pin
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Initialize the LCD 16*2
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
SDA_PIN = 0
SCL_PIN = 1
try:
    print("Initialize the LCD 16*2")
    i2c = I2C(0, sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    lcd.putstr("It Connect!")
    utime.sleep(2)
except Exception as e:
    print("Error: {}".format(e))
    print("Check the LCD 16*2 connection")
    utime.sleep(2)
    sys.exit()

# Initialize the DHT11 sensor
DHT11_DATA_PIN = 15
dht_pin = machine.Pin(DHT11_DATA_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
try:
    dht_sensor = dht.DHT11(dht_pin)
except Exception as e:
    print("Error: {}".format(e))
    print("Check the DHT connection")
    utime.sleep(2)
    sys.exit()

# Define pin for LED
LED_PIN = 5
led = Pin(LED_PIN, Pin.OUT)

# Define pin for button
BUTTON_PIN01 = 6
BUTTON_PIN02 = 7
BUTTON_PIN03 = 8

button01 = Pin(BUTTON_PIN01, Pin.IN, Pin.PULL_UP)
button02 = Pin(BUTTON_PIN02, Pin.IN, Pin.PULL_UP)
button03 = Pin(BUTTON_PIN03, Pin.IN, Pin.PULL_UP)


# fuction to read the status of the button01
def read_button01():
    if button01.value() == 0:
        LED_PIN.value(1)
        lcd.putstr("NATHEE SRINA\n")
        utime.sleep(5)
        lcd.clear()
    else:
        LED_PIN.value(0)


# function to read the status of the button02
def read_button02():
    if button02.value() == 0:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        lcd.putstr("Temp: {}C\n".format(temperature))
        lcd.putstr("Humidity: {}%".format(humidity))
        utime.sleep(5)
        lcd.clear()


# function to read the status of the button03
def read_button03():
    if button03.value() == 0:
        LED_PIN.value(1)
        lcd.putstr("LED ON\n")
        utime.sleep(5)
        lcd.clear()
    else:
        LED_PIN.value(0)


while True:
    try:
        lcd.putstr("Program Ready\n")
        read_button01()
        read_button02()
        read_button03()
    except Exception as e:
        print("Error: {}".format(e))
        print("Check the LCD OR DHT connection")
        utime.sleep(2)
        sys.exit()
