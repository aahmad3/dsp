import numpy as np
import matplotlib.pyplot as plt

# Setting up the variables
analog_samples = 1000
analog_sr = 1 / analog_samples
x = np.linspace(0, 1, analog_samples)
sig_freq = 10
sig = np.cos(2 * np.pi * sig_freq * x)
sampling_times = [0.01, 0.05, 0.1]
sampling_rates = np.divide(1, sampling_times).astype(int)

# first sampling
nt1 = (np.arange(0,1,0.01))
n1 = (nt1*1000).astype(int)
s1 = sig[n1]
plt.stem(n1,s1)
plt.show()

# second sampling
nt2 = (np.arange(0,1,0.05))
n2 = (nt2*1000).astype(int)
s2 = sig[n2]
plt.stem(n2,s2)
plt.show()

# third sampling
nt3 = (np.arange(0,1,0.1))
n3 = (nt3*1000).astype(int)
s3 = sig[n3]
plt.stem(n3,s3)
plt.show()
