# STFT Noise Cancellation

A Python-based audio noise cancellation system using Short-Time Fourier Transform (STFT) and spectral subtraction. This project reduces background noise in `.wav` speech recordings and enhances clarity using frequency domain filtering.

## 🔍 Features

- Applies STFT to analyze the frequency content of audio signals
- Performs noise estimation using spectral subtraction
- Applies bandpass filtering (300 Hz – 3400 Hz) to isolate human speech
- Uses gain adjustment and post-processing to improve clarity
- Outputs denoised `.wav` file with significantly reduced background noise

## 🛠 Tech Stack

- Python
- NumPy
- SciPy (STFT, ISTFT, filters)
- WAV file processing

## 📂 File Structure

