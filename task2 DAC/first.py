import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

DACPins = [22, 27, 17, 26, 25, 21, 20, 16]
GPIO.setup(DACPins, GPIO.OUT)
GPIO.output(DACPins, 0)

MaxV = 3.3

vol = 0

def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]


def vol_to_num(vol):
    if not (0.0 <= vol <= MaxV):
        print(f"too much voltage mf ( 0.00 - {MaxV:.2f} ) B")
        print("set 0.00 volts ")
        return 0
    return int(vol / MaxV * 255)

try:
    while True:
        try:
            vol = float(input("Set your voltage: "))
            num = vol_to_num(vol)
            GPIO.output(DACPins, dec2bin(num))
        
        except ValueError:
            print("Something bad happened")

finally:
    GPIO.output(DACPins, 0)
    GPIO.cleanup()

