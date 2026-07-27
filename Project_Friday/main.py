import speech_recognition as sr
import webbrowser
import pyttsx3

import sounddevice
import faster_whisper

recognizer = sr.Recognizer()
engine = pyttsx3.init()


# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"
def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Initializing Jarvis... ")

while True:

    # command initializing
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        audio = r.listen(source)
    print("recognizing....")
    # recognize speech using Sphinx
    try:
        command = sr.recognize_google_(audio)
        print(command)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
