import utime  # utime is a MicroPython module
import sys
from machine import I2C  # I2C is a MicroPython module for I2C communication
from machine import Pin  # Pin is a MicroPython module for GPIO pin control
from lcd_api import LcdApi  # LcdApi is a MicroPython module for LCD control
from pico_i2c_lcd import I2cLcd  # I2cLcd is a MicroPython module for LCD control
import dht  # dht is a MicroPython module for DHT11 sensor control

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


def runPGM_main():
    while True:
        try:
            # Display the readings on the LCD
            lcd.clear()
            # Read temperature and humidity from the DHT11 sensor
            dht_sensor.measure()
            temperature = dht_sensor.temperature()
            humidity = dht_sensor.humidity()

            # lcd.set_cursor(0, 0)
            lcd.putstr("Temp: {}C\n".format(temperature))
            # lcd.set_cursor(0, 1)
            lcd.putstr("Humidity: {}%".format(humidity))

            # Wait for a few seconds before taking the next reading
            utime.sleep(2)
        except Exception as e:
            print("Error: {}".format(e))
            print("Check the LCD OR DHT connection")
            utime.sleep(2)
            sys.exit()


# run the main program
runPGM_main()
