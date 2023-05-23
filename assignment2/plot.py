# !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# parameters to modify
filename="processed_iperf3_1.txt"
label='TCP'
xlabel = 'time/sec'
ylabel = 'measured bandwidth/Mbits/sec'
title='TCP: Bandwidth'
fig_name='iperf3_1.png'


t = np.loadtxt(filename, delimiter=" ", dtype="float")
plt.plot(t, label=label)
#plt.plot(t[:,0], t[:,1], label=label)  # Plot some data on the (implicit) axes.
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()
plt.savefig(fig_name)
plt.show()
