import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_freq = 10
sampling_freq = 1000

try:
    dac = r2r.R2R_DAC([16,20,21,25,26,17,27,22], 3.290, True)

    while True:
        signal = sg.get_sin_wave_amplitude(2, time.time)
        dac.set_voltage(signal)

finally:
    dac.deinit()