import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range  = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12 ,25 , 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def getvol(self):
        return GPIO.input(self.comp_gpio)

    def dec2bin(self, num):
        return [int(elem) for elem in bin(num)[2:].zfill(8)]

    def number_to_dac(self, num):
        GPIO.output(self.bits_gpio, self.dec2bin(num))

    def dec2vol(self, num):
        return (num/255)*self.dynamic_range

    def sequential_counting_adc(self):
        number = 0
        while(number < 255 and GPIO.input(self.comp_gpio) < 0.5):
            self.number_to_dac(number)
            number += 1
            time.sleep(self.compare_time)   
        self.number_to_dac(0)     
        return number
    
    def successive_approximation_adc(self, iterations):
        curr = 128
        delta = 128
        self.number_to_dac(int(curr))
        n = 1
        while (n < iterations):
            delta = delta/2
            if GPIO.input(self.comp_gpio) < 0.5:
                curr -= delta
            else:
                curr += delta
            self.number_to_dac(int(curr))
            n += 1
            time.sleep(self.compare_time)
        self.number_to_dac(0)
        return curr



if __name__ == "__main__":
    
    adc = R2R_ADC(3.2)
    
    try:
        while (True):
            print(adc.dec2vol(adc.sequential_counting_adc()))

    finally:
        adc.deinit()