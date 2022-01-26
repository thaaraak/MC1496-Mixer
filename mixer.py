from scipy import signal
from matplotlib import pyplot as plt
import numpy as np


frequency_a = 5000
frequency_b = 7000

sample_time = 0.005
samples = 1000

x = np.linspace( 0, sample_time, samples, endpoint=True )

sig_a = np.sin( 2 * np.pi * frequency_a * x )
sig_b = np.sin( 2 * np.pi * frequency_b * x )

plt.plot( sig_a * sig_b )
#plt.plot( sig_b )

plt.show()

