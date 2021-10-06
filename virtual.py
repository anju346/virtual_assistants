import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speak("Good morning ")
    elif hour>=12 and hour<16:
        speak("Good afternoon")
    else:
        speak("Good Evening ")

    speak("I am your Assistant Alexa")

def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry, can you repeat that again?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()
        if 'wikipedia' in query:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("youtube is opened")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("google is opened")
        elif 'open gmail' in query:
            webbrowser.open("www.gmail.com")
            speak("gmail is opened")
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
            speak("wikipedia is opened")
        elif 'play music' in query:
            music_dir = 'C:\\Users\chira\Documents\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("music is being played")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\chira\Desktop\mainproject"
            os.startfile(codepath)
        elif 'stop' in query:
            speak("see you soon")
            exit()
        else :
            webbrowser.open(query)
