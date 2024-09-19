import numpy as np
import matplotlib.pyplot as plt

# Carrier signal parameters
fc = 1000  # Carrier frequency in Hz
Ac = 1.0   # Carrier amplitude

# Message signal parameters
fm = 200   # Message frequency in Hz
Am = 0.5   # Message amplitude

# Modulation index
m = Am / Ac

# Sampling frequency
Fs = 10*fm  # Sampling frequency should be at least 10 times the highest frequency

# Time vector
t = np.arange(0, 1, 1/Fs)  # From 0 to 1 second with a step of 1/Fs

# Generate carrier signal
carrier = Ac * np.sin(2 * np.pi * fc * t)

# Generate message signal
message = Am * np.sin(2 * np.pi * fm * t)

# Calculate amplitude-modulated signal
am_signal = (1 + m*message) * carrier

# Plot the signals
fig, axs = plt.subplots(3)

axs[0].plot(t, message)
axs[0].set_ylabel('Message signal')
axs[0].set_xlabel('Time (s)')

axs[1].plot(t, carrier)
axs[1].set_ylabel('Carrier signal')
axs[1].set_xlabel('Time (s)')

axs[2].plot(t, am_signal)
axs[2].set_ylabel('AM signal')
axs[2].set_xlabel('Time (s)')

plt.show()