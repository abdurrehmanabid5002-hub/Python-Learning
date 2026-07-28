import webbrowser
import songs
import requests
from weather import get_weather
from speech import speak


def command_process(c):
    print("Received command:", c)

    if "open google" in c.lower():
        print("Opening GOOGLE")
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
        song = c.lower().split(" ", 1)[1]
        link=songs.music[song]
        webbrowser.open(link)
    # initilazing wether report 
    elif "weather" in c.lower():

        city = (
            c.lower()
            .replace("weather in", "")
            .replace("what's the weather in", "")
            .replace("what is the weather in", "")
            .replace("weather", "")
            .strip()
        )

        if city == "":
            city = "Sargodha"   # Default city if none is provided

        report = get_weather(city)
        print(report)
        speak(report)
