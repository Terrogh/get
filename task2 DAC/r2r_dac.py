import RPi.GPIO as GPIO

class R2R_DAC:

    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def vol_to_num(self, vol):
        if not (0.0 <= vol <= self.dynamic_range):
            print(f"too much voltage mf ( 0.00 - {self.dynamic_range:.2f} ) B")
            print("sets 0.00 volts ...")
            return 0
        return int(vol / self.dynamic_range * 255)

    def dec2bin(self, num):
        return [int(elem) for elem in bin(num)[2:].zfill(8)]

    def set_number(self, num):
        GPIO.output(self.gpio_bits, self.dec2bin(num))

    def set_voltage(self, vol):
        self.set_number(self.vol_to_num(vol))

if __name__ == "__main__":
    
    dac = R2R_DAC([16,20,21,25,26,17,27,22], 3.183, True)
    
    try:

        while True:
            try:
                vol = float(input("set voltage in volts: "))
                dac.set_voltage(vol)

            except ValueError:
                print("Not a number, try again mf")

    finally:
        dac.deinit()

        
        
