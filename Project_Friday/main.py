import speech_recognition as sr
import webbrowser
import pyttsx3
import songs
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from commands import command_process
from speech import speak
import pyttsx3
engine = pyttsx3.init()

# Recognizer 
recognizer = sr.Recognizer()



# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"



if __name__ == "__main__":
    speak("Initializing Friday... ")

    while True:

        # command initializing
        # obtain audio from the microphone
        
    
        print("recognizing....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listing...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            word = recognizer.recognize_google(audio)
            print("You said:", word)
            if "friday" in word.lower():
                print("Wake word detected")
                engine.say("Friday at your service...")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    print("Friday at your service...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    command_process(command)
        except sr.UnknownValueError:
            print("Friday could not understand audio")
        except sr.RequestError as e:
            print(" error; {0}".format(e))
