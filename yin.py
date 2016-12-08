import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np

fs, data = wavfile.read("../A1_bass.wav")

print(fs)

fig = plt.figure()
g1 = fig.add_subplot(221)
g1.set_title("Original signal")
g1.plot(data)


g2 = fig.add_subplot(222)
g2.set_title("FFT")
s = fft(data)
k = np.arange(len(data))
T = len(data)/fs
frqLabel = k/T

g2.plot(frqLabel[:500], abs(s[:500]))
g2.grid(b=True, which='both', color='0.65')



# autocorrelation thing
tau_max = 3000
w_size = 6000
r = np.zeros(tau_max)
for i in range(tau_max):
    s = 0.0
    for j in range(w_size):
        s += (data[j] - data[j+i]) * (data[j] - data[j+i])
    r[i] = s

g3 = fig.add_subplot(223)
g3.set_title("Difference function")
g3.plot(r)

# d` calculation
d = np.zeros(tau_max)
s = r[0]
d[0] = 1
for i in range(1,tau_max):
    s += r[i]
    d[i] = r[i] / ((1 / i) * s) 

g4 = fig.add_subplot(224)
g4.set_title("Normalized diff func")
g4.plot(d)

plt.show()

# find frequency. use 0.5 as threshold

for i in range(tau_max):
    if d[i] > 0.5:
        continue
    if d[i-1] > d[i] < d[i+1]:
        print(44100/i)
        break


