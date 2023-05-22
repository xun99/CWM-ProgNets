import numpy as np
import matplotlib.pyplot as plt

t = np.loadtxt("processed_ping_test5_1", delimiter=" ", dtype="float")

for number # !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# parameters to modify
filename="processed_ping_test5_1"
label='label'
xlabel = 'xlabel'
ylabel = 'ylabel'
title='Simple plot'
fig_name='cdf.png'


t = np.loadtxt(filename, delimiter=" ", dtype="float")

t = np.sort(y)
y = 1. * np.arange(len(data)) / (len(data) - 1)
plt.plot(t, y)

"""
plt.plot(t[:,0], t[:,1], label=label)  # Plot some data on the (implicit) axes.
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()
plt.savefig(fig_name)
"""
plt.show()

