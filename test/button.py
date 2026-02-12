import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LEDPin = 26

GPIO.setup(LEDPin, GPIO.OUT)

ButtPin = 13

GPIO.setup(ButtPin, GPIO.IN)

isLEDon = 0

while True:
    if GPIO.input(ButtPin):
        isLEDon = not isLEDon
        GPIO.output(LEDPin, isLEDon)
        time.sleep(0.1)
    else:
        GPIO.output(LEDPin, 0)