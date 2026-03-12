import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LEDPins = [26, 20, 19, 16, 13, 12 ,25 , 11]
GPIO.setup(LEDPins, GPIO.OUT)
GPIO.output(LEDPins, 0)