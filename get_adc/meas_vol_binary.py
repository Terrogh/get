import r2r_adc as r2r

adc = r2r.R2R_ADC(3.2, 0.1)

voltage_values = []
time_values = []

try:
    while (True):
        print(adc.dec2vol(adc.successive_approximation_adc(7)))
finally:
    adc.deinit()