from machine import Pin
from utime import ticks_ms, ticks_diff

led = Pin(14, Pin.OUT)
interval = 500  # milliseconds

while True:
    led.on()
    start_time = ticks_ms()
    while ticks_diff(ticks_ms(), start_time) < interval:
        pass
    led.off()
    start_time = ticks_ms()
    while ticks_diff(ticks_ms(), start_time) < interval:
        pass