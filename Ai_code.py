import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import urllib.parse
import psutil
import pyjokes
import sys

en = pyttsx3.init()

voices = en.getProperty('voices')
en.setProperty('voice', voices[1].id)


def speak(audio):
    print("AI:", audio)
    en.say(audio)
    en.runAndWait()


speak("Hey, this is an AI assistant")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The time in 24-hour format is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The date is")
    speak(date)
    speak("The month is")
    speak(month)
    speak("The year is")
    speak(year)

def wishme():
    speak("Welcome back")

    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 15:
        speak("Good afternoon")
    elif 15 <= hour < 20:
        speak("Good evening")
    elif 20 <= hour < 24:
        speak("Good night")
    else:
        speak("Good night")
    speak("AI is at your service. How can I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)

    except Exception as e:
        print(e)
        speak("Sorry, could you say that again?")
        return "none"
    return query



def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU usage is " + usage + " percent")


def jokes():
    joke = pyjokes.get_joke()
    speak(joke)


def name():
    speak("My name is AI")
    

def boss():
    speak("Boss")
    

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'time' in query:
            time()
        elif 'boss' in query:
            boss()
        elif 'date' in query:
            date()
        elif 'name' in query:
            name()
        elif 'wikipedia' in query:
            speak("I am searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            

        elif 'search' in query:
            speak("What do you want to search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takecommand().lower()
            search_query = urllib.parse.quote(search)
            wb.get(chromepath).open_new_tab("https://www.google.com/search?q=" + search_query)

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'note this one' in query:
            speak("What should I remember?")
            data = takecommand()
            speak("You said me to remember that " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that " + remember.read())
            print("You said me to remember that", remember.read())

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()
            speak("It's really good, right? Hahaha")

        elif "offline" in query:
            speak("Okay, done!")
            sys.exit()
