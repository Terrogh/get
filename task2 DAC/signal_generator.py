import numpy as np
import time

def get_sin_wave_amplitude(frequency, time):
    thing2 = 3.1415
    thing = 2.0*thing2*frequency*time() + 1.0
    return ( np.sin(thing) + 1.0 )/2.0

def wait_for_sampling_period(sampling_freq):
    time.sleep(2*3.1415*sampling_freq)
