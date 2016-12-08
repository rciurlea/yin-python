import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np

fs, data = wavfile.read("E2_bass.wav")

print(fs)

plt.subplot(221)
plt.plot(data)

plt.subplot(222)
s = fft(data)
k = np.arange(len(data))
T = len(data)/fs
frqLabel = k/T

plt.plot(frqLabel[:500], abs(s[:500]))
plt.grid(b=True, which='both', color='0.65')



# autocorrelation thing
tau_max = 3000
w_size = tau_max
r = np.zeros(tau_max)
for i in range(tau_max):
    s = 0.0
    for j in range(w_size):
        s += (data[j] - data[j+i]) * (data[j] - data[j+i])
    r[i] = s

plt.subplot(223)
plt.plot(r)

# d` calculation
d = np.zeros(tau_max)
s = r[0]
d[0] = 1
for i in range(1,tau_max):
    s += r[i]
    d[i] = r[i] / ((1 / i) * s) 

plt.subplot(224)
plt.plot(d)

plt.show()
