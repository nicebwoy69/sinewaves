import numpy as np
import matplotlib.pyplot as plt

# Define time array
t = np.linspace(0, 1, 500)

# Define frequency and amplitudes for the waves
frequency = 5  # in Hz
amplitude = 1.0
phase_shift_constructive = 0  # 0 degrees, in phase
phase_shift_destructive = np.pi  # 180 degrees, out of phase

# Generate waveforms for constructive and destructive interference
wave1 = amplitude * np.sin(2 * np.pi * frequency * t)
wave2_constructive = amplitude * np.sin(2 * np.pi * frequency * t + phase_shift_constructive)
wave2_destructive = amplitude * np.sin(2 * np.pi * frequency * t + phase_shift_destructive)

# Combined waveforms
combined_constructive = wave1 + wave2_constructive
combined_destructive = wave1 + wave2_destructive

# Plot Constructive Interference
plt.figure(figsize=(10, 6))
plt.plot(t, wave1, '--', label='Wave 1')
plt.plot(t, wave2_constructive, '--', label='Wave 2 (In Phase)')
plt.plot(t, combined_constructive, label='Combined (Constructive)')
plt.title("Constructive Interference")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.savefig("constructive_interference.png")
plt.show()

# Plot Destructive Interference
plt.figure(figsize=(10, 6))
plt.plot(t, wave1, '--', label='Wave 1')
plt.plot(t, wave2_destructive, '--', label='Wave 2 (Out of Phase)')
plt.plot(t, combined_destructive, label='Combined (Destructive)')
plt.title("Destructive Interference")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.savefig("destructive_interference.png")
plt.show()
