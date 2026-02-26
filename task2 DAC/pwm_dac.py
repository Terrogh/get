import RPi.GPIO as GPIO

class PWM_DAC:

    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

        PWM_DAC.PWM = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        PWM_DAC.PWM.start(0.0)
        

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def vol_to_num(self, vol):
        if not (0.0 <= vol <= self.dynamic_range):
            print(f"too much voltage mf ( 0.00 - {self.dynamic_range:.2f} ) B")
            print("sets 0.00 volts ...")
            return 0
        return vol / self.dynamic_range * 100

    def set_voltage(self, vol):
        num = self.vol_to_num(vol)
        # print(f"num = {num:.2f}")
        PWM_DAC.PWM.ChangeDutyCycle(num)

if __name__ == "__main__":
    
    dac = PWM_DAC(12, 500, 3.290, True)

    try:

        while True:
            try:
                vol = float(input("set voltage in volts: "))
                dac.set_voltage(vol)

            except ValueError:
                print("Not a number, try again mf")

    finally:
        dac.deinit()
