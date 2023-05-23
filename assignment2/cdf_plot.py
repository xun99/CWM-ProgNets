import numpy as np
import matplotlib.pyplot as plt

# !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# parameters to modify
filename="processed_ping_test5_3.txt"
label='label'
xlabel = 'rtt'
ylabel = 'probability'
title='Ping Test: interval 0.0001'
fig_name='cdf3.png'


t = np.loadtxt(filename, delimiter=" ", dtype="float")

t = np.sort(t)
y = 1. * np.arange(len(t)) / (len(t) - 1)
plt.plot(t, y, label=label)

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()
plt.savefig(fig_name)
plt.show()

