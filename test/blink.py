import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LEDPin = 26

GPIO.setup(LEDPin, GPIO.OUT)

flag = False

while True:
    flag = not flag
    GPIO.output(LEDPin, flag)
    time.sleep(1)

    