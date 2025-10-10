import numpy as np
import matplotlib.pyplot as plt
import math


# def generate_cont_signal(type,amplitude,phase_deg,freq):
#     phase_rad = math.radians(phase_deg)
#     x = np.linspace(0, 5, 1000)
#     y=[]
#     if type == 's':
#         y = amplitude* np.sin((2*math.pi*freq*x)+phase_rad)
#     else:
#         y = amplitude* np.cos((2*math.pi*freq*x)+phase_rad)
#     return x,y


# x,y = generate_cont_signal('c',10,0,1)
def generate_signal(signal_type, representation, amplitude, phase_deg, freq, fs=None, duration=1):
    phase_rad = math.radians(phase_deg)
    if representation == 'continuous':
        t = np.linspace(0, duration, 1000)
        if signal_type == 's':
            y = amplitude * np.sin(2 * math.pi * freq * t + phase_rad)
        else:
            y = amplitude * np.cos(2 * math.pi * freq * t + phase_rad)
    elif representation == 'discrete':
        if fs is None:
            raise ValueError("Sampling frequency fs must be provided for discrete signal.")
        if fs < 2 * freq:
            print("Sampling frequency violates Nyquist theorem")
        n = np.arange(0, duration, 1/fs)
        if signal_type == 's':
            y = amplitude * np.sin(2 * math.pi * freq * n + phase_rad)
        else:
            y = amplitude * np.cos(2 * math.pi * freq * n + phase_rad)
        t = n 
    else:
        raise ValueError("representation must be either 'continuous' or 'discrete'")
    return t, y


# print(len(x))
# print(len(y))

# plt.plot(x, y, color='blue')  # Use line plot
# plt.title("Smooth (Continuous) Sine Wave")
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.grid(True)
# plt.show()