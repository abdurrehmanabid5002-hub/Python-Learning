import speech_recognition as sr
import webbrowser
import pyttsx3
import songs
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()


# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"
def speak(text):
    engine.say(text)
    engine.runAndWait()


def command_process(c):
    print(c)

    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open x" in c.lower() or "open twitter" in c.lower():
        webbrowser.open("https://x.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=songs.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        response=requests.get()


if __name__ == "__main__":
    speak("Initializing Friday... ")

while True:

    # command initializing
    # obtain audio from the microphone
    r = sr.Recognizer()
   
    print("recognizing....")
    # recognize speech using Sphinx
    try:
        with sr.Microphone() as source:
            print("Listing...")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)
        word = r.recognize_google(audio)
        if word.lower() == "friday":
            speak("At your service")
            with sr.Microphone() as source:
                print("Friday at your service...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                command_process(command)
    except sr.UnknownValueError:
        print("Friday could not understand audio")
    except sr.RequestError as e:
        print(" error; {0}".format(e))
