try:
    import machine
    import utime

except ImportError:
    print("Error: 'machine' module not found. Make sure you are using MicroPython.")
    exit()

sdaPIN = machine.Pin(0)
sclPIN = machine.Pin(1)
i2c = machine.I2C(0, sda=sdaPIN, scl=sclPIN, freq=400000)
while True:
    devices = i2c.scan()
    if len(devices) == 0:
        print("No i2c device !")
    else:
        print("i2c devices found:", len(devices))
    for device in devices:
        print("Hexa address: ", hex(device))
    utime.sleep(1)
