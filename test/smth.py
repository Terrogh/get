import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LEDPin = 26
GPIO.setup(LEDPin, GPIO.OUT)

VolDivPin = 6
GPIO.setup(VolDivPin, GPIO.IN)

while True:
    GPIO.output(LEDPin, not GPIO.input(VolDivPin))