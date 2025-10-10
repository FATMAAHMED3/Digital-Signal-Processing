import numpy as np
import matplotlib.pyplot as plt
import math


def generate_cont_signal(type,amplitude,phase_deg,freq):
    phase_rad = math.radians(phase_deg)
    x = np.linspace(0, 5, 1000)
    y=[]
    if type == 's':
        y = amplitude* np.sin((2*math.pi*freq*x)+phase_rad)
    else:
        y = amplitude* np.cos((2*math.pi*freq*x)+phase_rad)
    return x,y


x,y = generate_cont_signal('c',10,0,1)

print(len(x))
print(len(y))

# plt.plot(x, y, color='blue')  # Use line plot
# plt.title("Smooth (Continuous) Sine Wave")
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.grid(True)
# plt.show()