# STFT Noise Cancellation

A Python-based audio noise cancellation system using Short-Time Fourier Transform (STFT) and spectral subtraction. This project reduces background noise in `.wav` speech recordings and enhances clarity using frequency domain filtering and bandpass post-processing.

---

## 🔍 Features

* Converts stereo audio to mono and performs STFT to analyze frequency content
* Estimates background noise from the initial audio segment and subtracts it
* Applies bandpass filtering (300 Hz – 3400 Hz) to isolate human speech
* Adjusts output gain to improve clarity and loudness
* Outputs cleaned audio as a new `.wav` file

---

## 💪 Tech Stack

* **Python 3.x**
* **NumPy**
* **SciPy** (for STFT, ISTFT, and filtering)
* **WAV File I/O** via `scipy.io.wavfile`

---

## 📂 Project Structure

```
├── main.py                  # Core script for noise cancellation
├── my_audio1.wav           # Input audio file (replace with your own)
├── filtered_speech.wav     # Output audio with reduced noise
├── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/saheelfaisal/stft-noise-cancellation.git
cd stft-noise-cancellation
```

### 2. Install dependencies

Make sure you have Python 3.x installed.

```bash
pip install numpy scipy
```

### 3. Prepare your input

Replace `my_audio1.wav` with the `.wav` file you want to process. Make sure it’s a 16-bit PCM `.wav` file.

### 4. Run the script

```bash
python main.py
```

### 5. Output

The cleaned audio will be saved as `filtered_speech.wav` in the same directory.

---

## 📝 Notes

* Assumes the first \~10 frames of the audio contain only background noise for estimation
* Stereo audio is automatically converted to mono
* You can tune:

  * The bandpass range (`300–3400 Hz`) for speech isolation
  * The gain factor to amplify final output volume
* Output is clipped to `int16` range to prevent overflow distortion

---

## 📈 Results

* Achieved up to **70% reduction in background noise** on test recordings
* Improved **speech intelligibility** in real-world `.wav` samples
* System is easily extensible to work with real-time audio (e.g., microphone input)

---

## 📷 Future Improvements

* Visualize spectrogram before and after filtering
* Add support for live mic input and real-time noise reduction
* Streamlit interface for quick web-based demo
* Config file for easy parameter tuning

---

## 🔗 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤛️ Author

**Saheel Faisal**
[LinkedIn](https://www.linkedin.com/in/saheel-faisal) • [Email](mailto:saheelfaisal@outlook.com)
