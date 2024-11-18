# Tutorial 8: Sinusoidal Signals, Phase, and Addition of Sinusoids

---

## 1. Key Properties of Sinusoidal Signals

A **sinusoid** represents the simplest form of an audio signal, with a single frequency, such as a pure tone. Sinusoids are foundational to more complex waveforms and are used to build complex sounds through synthesis or analysis.

### Basic Components of a Sinusoid
- **Amplitude (A)**: The maximum value of the wave, determining the loudness or intensity.
- **Period (T)**: The time to complete one cycle, measured in seconds.
- **Frequency (f)**: The number of cycles per second, measured in Hertz (Hz), calculated as:
  
  \[
  f = \frac{1}{T}
  \]

**Example of Sinusoid Frequencies**:
- A sinusoid with \( T = 0.25 \, \text{s} \) has \( f = 4 \, \text{Hz} \).
- In audio, common frequencies include 100 Hz (bass), 1 kHz (mid), and 10 kHz (high frequencies).

### Chart Placeholder
- **Chart of Sinusoid Frequencies**: This chart will show amplitude, period, and frequency relationships.

---

## 2. Fourier Transform Analysis and Sinusoidal Components

**Fourier Transform** decomposes complex signals into individual sinusoids, each with specific **frequency, amplitude,** and **phase**. This analysis is crucial for sound synthesis, signal processing, and audio engineering.

### Example of Fourier Transform
A complex signal could be expressed as:

\[
A(t) = A_1 \sin(2 \pi f_1 t) + A_2 \sin(2 \pi f_2 t) + \dots
\]

where each component represents a sinusoid with amplitude \( A \), frequency \( f \), and phase \( \phi \).

### Chart Placeholder
- **Fourier Transform Breakdown**: Chart showing decomposition of a complex signal into frequency components with individual amplitudes and phases.

---

## 3. Phase and Phase Delay in Sinusoids

**Phase** (\( \phi \)) represents a specific point within a cycle of a sinusoid, commonly measured in **radians** or **degrees**. Phase is important in aligning signals and understanding interference.

### Phase Delay
When one wave lags behind another, a **time delay** is introduced, resulting in a **phase shift**. The relationship is given by:

\[
\phi = -2 \pi f t_D
\]

where \( f \) is frequency in Hz, and \( t_D \) is the time delay in seconds.

### Phase Conversion
- **Radians to Degrees**:
  \[
  1 \text{ radian} = \frac{180^\circ}{\pi}
  \]
- **Example Conversions**:
  - \( 0^\circ = 0 \, \text{radians} \)
  - \( 90^\circ = \frac{\pi}{2} \, \text{radians} \)
  - \( 180^\circ = \pi \, \text{radians} \)
  - \( 360^\circ = 2\pi \, \text{radians} \)

### Table Placeholder
- **Table of Radian to Degree Conversions**: This table will list conversions for key phase angles.

### Example Calculation for Phase Delay
Given a signal with:
- **Frequency** = 10 Hz
- **Time delay** = 150 ms

Convert time delay to seconds: \( t_D = 0.15 \, \text{s} \)

Calculate phase shift:

\[
\phi = -2 \pi \times 10 \times 0.15 = -9.42 \, \text{radians}
\]

---

## 4. Adding Sinusoids: Correlated vs. Uncorrelated Signals

### Adding Correlated Sinusoids
**Same Frequency**: Correlated sinusoids have the same frequency but can vary in amplitude or phase.

#### In-Phase Addition
- Amplitudes add linearly.
- Example: If two sinusoids of amplitude 1 are added in-phase, resulting amplitude = 2.

#### Out-of-Phase Addition
- Phase differences affect the resulting amplitude.
- Example: Adding two sinusoids of amplitude 1 with a 90° phase difference results in a peak amplitude of approximately 1.4.

### Adding Uncorrelated Sinusoids
**Different Frequencies**: When frequencies differ, the resulting waveform is complex.

- **Harmonic Frequencies**: Each component is perceived separately, e.g., 100 Hz and 200 Hz.
- **Non-Harmonic Frequencies**: Results in amplitude modulation (AM) at the frequency difference.

#### Example Calculation
Adding 500 Hz and 490 Hz creates a modulated signal with a 10 Hz modulation frequency.

### Chart Placeholder
- **Correlated vs. Uncorrelated Addition**: Chart showing differences in amplitude, phase, and modulation effects for correlated and uncorrelated signals.

---

## 5. Practical Applications of Sinusoidal Addition

### Phase Delay in Signal Processing
Used to align signals or add effects, such as in reverb or echo.

### Fourier Analysis in Audio Engineering
Decomposes signals into sinusoids, guiding frequency adjustments in EQ, compression, and mixing.

### Adding Sinusoids in Mixing and Sound Design
- **In-Phase Addition**: Boosts amplitude for specific effects.
- **Out-of-Phase Addition**: Modulation produces varied textures in sound.

### Example Placeholder
- **Example of Uncorrelated Sinusoid Addition in Sound Design**: Example illustrating how two uncorrelated sinusoids interact to create a new texture or modulation effect.

---

## Summary

- **Sinusoids** form the basis for all periodic signals, essential for analyzing and synthesizing sounds.
- **Fourier Transform** enables breakdown into frequency components.
- **Phase and Time Delay**: Critical for controlling interference and alignment in multi-signal systems.
- **Correlated and Uncorrelated Addition**: Determines resulting waveform characteristics, from simple sums to complex modulations.

### Table Placeholder
- **Summary Table of Sinusoidal Properties and Concepts**: Summarizes the main properties, calculations, and applications covered in the tutorial.

