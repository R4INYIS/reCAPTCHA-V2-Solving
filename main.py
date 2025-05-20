import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr
from time import sleep
import requests
import subprocess
import os

#* Functions

def switch_to_iframe(driver):
    """
    Switches Selenium's context to the second Google iframe on the page.
    This is necessary to interact with reCAPTCHA elements.
    """
    driver.switch_to.default_content()
    iframes = driver.find_elements(By.XPATH, '//iframe[contains(@src, "google.com")]')
    driver.switch_to.frame(iframes[1])

#? Constants

URL: str = "https://2captcha.com/es/demo/recaptcha-v2"  # Demo page with reCAPTCHA

ID_BUTTON: str = "recaptcha-anchor" # Default ID recaptcha-anchor
ID_AUDIO: str = "recaptcha-audio-button" # Default ID recaptcha-audio-button
ID_AUDIO_RESPONSE: str = "audio-response" # Default ID audio-response
ID_AUDIO_SEND: str = "recaptcha-verify-button" # Default ID recaptcha-verify-button

AUDIO_PATH: str = r".\recaptcha V2\files"     # Path to store audio files
FFMPEG_PATH: str = r".\ffmpeg\bin\ffmpeg.exe" # Path to ffmpeg executable

#* Driver configuration

driver = uc.Chrome(log_level=0)               # Start undetected Chrome driver
driver.get(URL)                               # Open the demo page
wait = WebDriverWait(driver, 10)              # Explicit wait for elements

#! Captcha solving

# Click the reCAPTCHA checkbox to start the challenge
driver.switch_to.frame(
    wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src, "google.com")]')))
)
wait.until(EC.presence_of_element_located((By.ID, ID_BUTTON))).click()

# Try to solve the audio challenge
try:
    # Switch to the audio challenge iframe and click the audio button
    switch_to_iframe(driver)
    wait.until(EC.presence_of_element_located((By.ID, "recaptcha-audio-button"))).click()

    # Download the audio file from the challenge
    switch_to_iframe(driver)
    wavlink = wait.until(EC.presence_of_element_located((By.ID, ID_AUDIO))).get_attribute("src")
    img = requests.get(wavlink)
    open(f'{AUDIO_PATH}/audio.mp3', 'wb').write(img.content)
    sleep(5)

    # Convert the downloaded MP3 audio to WAV using ffmpeg
    subprocess.call([f'{FFMPEG_PATH}', '-i', f'{AUDIO_PATH}\\audio.mp3', f'{AUDIO_PATH}\\audio.wav'])

    # Use speech recognition to transcribe the audio challenge
    r = sr.Recognizer()
    with sr.AudioFile(r"./recaptcha V2/files/audio.wav") as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            # Submit the recognized text as the answer to the audio challenge
            driver.find_element(By.ID, ID_AUDIO_RESPONSE).send_keys(text)
            driver.find_element(By.ID, ID_AUDIO_SEND).click()
        except:
            print("ERROR")

    # Clean up audio files after processing
    os.remove(f'{AUDIO_PATH}/audio.mp3')
    os.remove(f'{AUDIO_PATH}/audio.wav')
except:
    print("CAPTCHA COMPLETION NOT NECESSARY")

sleep(5)