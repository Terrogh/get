import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LEDPins = [24, 22, 23, 27, 17, 25, 12, 16, 26]
GPIO.setup(LEDPins, GPIO.OUT)
GPIO.output(LEDPins, 0)