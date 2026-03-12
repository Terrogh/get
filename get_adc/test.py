import RPi.GPIO as GPIO
import r2r_adc

adc = r2r_adc.R2R_ADC(3.2)

LEDPins = [26, 20, 19, 16, 13, 12 ,25 , 11]
GPIO.setup(LEDPins, GPIO.OUT)
GPIO.output(LEDPins, 1)
