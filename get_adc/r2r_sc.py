import r2r_adc as r2r
import time
import adc_plot

adc = r2r.R2R_ADC(3.2, 0.0001)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()
    while (time.time() < start_time + duration):
        voltage_values = voltage_values + [adc.dec2vol(adc.sequential_counting_adc())]
        time_values = time_values + [time.time() - start_time]
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.2)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    r2r.deinit()
