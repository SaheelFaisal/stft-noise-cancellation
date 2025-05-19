import numpy as np
from scipy.io import wavfile
from scipy.signal import stft, istft, butter, lfilter

# Function to apply a bandpass filter to focus on the speech frequency range
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    
def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Load the audio file
sample_rate, audio_signal = wavfile.read('my_audio1.wav')

# If the audio is stereo, convert it to mono
if len(audio_signal.shape) > 1:
    audio_signal = np.mean(audio_signal, axis=1)

# Apply Short-Time Fourier Transform (STFT)
frequencies, times, stft_matrix = stft(audio_signal, fs=sample_rate, nperseg=1024)

# Estimate noise from the first segment (assuming it's noise only)
noise_estimation = np.mean(np.abs(stft_matrix[:, :10]), axis=1, keepdims=True)

# Subtract the noise estimate from the entire STFT matrix
stft_matrix_cleaned = stft_matrix - noise_estimation

# Ensure no negative magnitudes (optional step to avoid artifacts)
stft_matrix_cleaned = np.where(np.abs(stft_matrix_cleaned) < 0, 0, stft_matrix_cleaned)

# Apply Inverse Short-Time Fourier Transform (ISTFT)
_, filtered_signal = istft(stft_matrix_cleaned, fs=sample_rate)

# Optional: Apply a bandpass filter to focus on the frequency range of human speech (300 Hz to 3400 Hz)
filtered_signal = bandpass_filter(filtered_signal, 300, 3400, sample_rate)

# Adjust the volume by applying a gain factor
gain_factor = 2.0  # Increase this value to make the audio louder
filtered_signal = filtered_signal * gain_factor

# Clip values to the range of int16 to avoid overflow
filtered_signal = np.clip(filtered_signal, -32768, 32767)

# Save the filtered and amplified audio to a new file
wavfile.write('filtered_speech_louder.wav', sample_rate, np.int16(filtered_signal))

print("Noise filtering and volume adjustment completed. Saved as 'filtered_speech_louder.wav'")

# Save the filtered audio to a new file
wavfile.write('filtered_speech_stft.wav', sample_rate, np.int16(filtered_signal))

print("Noise filtering using STFT completed and saved as 'filtered_speech_stft.wav'")
