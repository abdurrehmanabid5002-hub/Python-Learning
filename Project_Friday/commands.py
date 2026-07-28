import webbrowser
import songs

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
    elif "news" in c.lower():
        response = requests.get("https://newsapi.org/...")