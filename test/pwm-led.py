import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LEDPin = 26
GPIO.setup(LEDPin, GPIO.OUT)

PWM = GPIO.PWM(LEDPin, 200)
PWMVal = 0.0
PWM.start(PWMVal)

while True:
    while PWMVal < 100.0:
        time.sleep(0.01)
        PWMVal += 1.0
        PWM.ChangeDutyCycle(PWMVal)
    while PWMVal > 1.0:
        time.sleep(0.01)
        PWMVal -= 1.0
        PWM.ChangeDutyCycle(PWMVal)