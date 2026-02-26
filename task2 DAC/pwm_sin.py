import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_freq = 10
sampling_freq = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.290, True)

    # PWM = GPIO.PWM(dac.gpio_pin, dac.pwm_frequency)
    # PWM.start(0.0)

    while True:
        signal = sg.get_sin_wave_amplitude(2, time.time)
        dac.set_voltage(signal)
                                                                                                           
finally:
    dac.deinit()
