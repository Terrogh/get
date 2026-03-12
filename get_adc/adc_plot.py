from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.xlabel("time")
    plt.ylabel("voltage")
    plt.xlim(0,5.0)
    plt.ylim(0,3.2)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
    i = 0
    while i < len(time) - 1:
        sampling_periods += [time[i + 1] - time[i]]
        i += 1
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.xlim(0,0.06)
    plt.show()
    


def dec2bin(self, num):
        return [int(elem) for elem in bin(num)[2:].zfill(8)]