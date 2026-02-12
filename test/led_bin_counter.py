import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LEDPins = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(LEDPins, GPIO.OUT)
GPIO.output(LEDPins, 0)

ButtUp = 9
GPIO.setup(ButtUp, GPIO.IN)
ButtDown = 10
GPIO.setup(ButtDown, GPIO.IN)

Number = 0

def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]

SleepTime = 0.1

while True:
    if GPIO.input(ButtUp):
        Number += 1
        if Number > 255:
            Number = 0
        print(Number, dec2bin(Number))
        time.sleep(SleepTime)
    if GPIO.input(ButtDown):
        Number -= 1
        if Number < 0:
            Number = 255
        print(Number, dec2bin(Number))
        time.sleep(SleepTime)
    GPIO.output(LEDPins, dec2bin(Number))