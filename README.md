## 🔊 reCAPTCHA v2 Solving – Automated Challenge Handler

This project is a Python-based tool that automates the process of solving **Google reCAPTCHA v2** using the **audio challenge** method. It leverages Selenium with `undetected-chromedriver` to bypass detection and uses **speech recognition** to transcribe and submit the audio response automatically.

---

### 📦 Features

* Detects and interacts with reCAPTCHA v2 challenges on websites.
* Navigates to the audio challenge automatically.
* Downloads the challenge audio and converts it to WAV format using `ffmpeg`.
* Transcribes the audio using Google’s speech recognition API.
* Submits the recognized response and attempts verification.
* Designed to mimic human-like interaction with reCAPTCHA.

---

### ✅ Requirements

* Python 3.8+
* Google Chrome
* Chromedriver (managed by `undetected-chromedriver`)
* [FFmpeg](https://ffmpeg.org/) (for audio format conversion)

#### Python Libraries

Install the required libraries using:

```bash
pip install selenium undetected-chromedriver SpeechRecognition requests
```

---

### ⚙️ Setup

1. **Clone the repository:**

```bash
git clone [https://github.com/R4INYIS/reCAPTCHA-V2-Solving/]
cd reCAPTCHA-V2-Solving
```

2. **Download and extract FFmpeg:**

Make sure the path to the FFmpeg executable is correctly set in the script:

```python
FFMPEG_PATH = r".\\ffmpeg\\bin\\ffmpeg.exe"
```

3. **Create folders:**

Ensure that the following directory exists:

```
./recaptcha V2/files
```

This folder will store the downloaded and converted audio files temporarily.

---

### ▶️ How to Run

Simply execute:

```bash
python main.py
```

The script will:

* Load the demo reCAPTCHA page
* Trigger the audio challenge
* Download and transcribe the audio
* Submit the response to attempt solving the CAPTCHA

---

### ⚠️ Disclaimer

This project is for **educational purposes only**. Bypassing CAPTCHA protections may violate terms of service of certain platforms. Use responsibly and only where authorized.

