import utime

import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16


def test_main():
    # Test function for verifying basic functionality
    print("Running test_main")
    i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    lcd.putstr("It Works!")
    utime.sleep(2)
    lcd.clear()
    count = 0
    while True:
        lcd.clear()
        time = utime.localtime()
        lcd.putstr(
            "{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}:{SS:>02d}".format(
                year=time[0],
                month=time[1],
                day=time[2],
                HH=time[3],
                MM=time[4],
                SS=time[5],
            )
        )
        print("Turning cursor on")
        utime.sleep(0.25)
        lcd.show_cursor()
        print("Turning cursor off")
        utime.sleep(0.25)
        lcd.hide_cursor()
        print("Turning blink cursor on")
        utime.sleep(0.25)
        lcd.blink_cursor_on()
        print("Turning blink cursor off")
        utime.sleep(0.25)


# if __name__ == "__main__":
test_main()
