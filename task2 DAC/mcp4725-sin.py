import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_freq = 10
sampling_freq = 1000

try:
    mcp = mcp.MCP4725(5.0)

    while True:
        signal = sg.get_sin_wave_amplitude(2, time.time)
        mcp.set_voltage(signal)

finally:
    mcp.deinit()