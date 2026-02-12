import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LEDPins = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(LEDPins, GPIO.OUT)
GPIO.output(LEDPins, 0)

JMPTime = 0.1

while True:
    for LEDPin in LEDPins:
        GPIO.output(LEDPin, 1)
        time.sleep(JMPTime)
        GPIO.output(LEDPin, 0)
    for LEDPin in reversed(LEDPins):
        GPIO.output(LEDPin, 1)
        time.sleep(JMPTime)
        GPIO.output(LEDPin, 0)