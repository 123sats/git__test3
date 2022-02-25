[1:59 pm, 20/02/2022] Mihir Narkar: import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



# audio function:-
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour>=18 and hour<20:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")

    speak("I am jarvis. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from user and reaturns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        speak("say that again please")
        return "None"
    return query

if _name_ == '_main_':
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2) 
            speak("According to wikipedia")
            print(results)
            speak(results)

        if "my age" in query:
            speak("You are 20 years old boy looking for girl")

        if "wish me" in query:
            wishMe()

        elif 'pubg or free fire' in query:
            speak("Pubg is proo game, and free fire is noob game")

        elif ('sister name' in query):
            speak("Searching for your sister...")
            speak("Your sister name is Riya rajendra pangam")

        elif('sister live' in query):
            speak("Your sister,called as riya lived in Virar next to nalasopara")
            
        elif('riya mobile health' in query):
            speak("No too good,  riyaa please replace mobile as soon as possible")

        elif ('my name' in query):
            speak("Your name is Mihir chandrakant Narkar, you build me, you are my god")

        elif 'quit' in query:
            speak("Thanks for your time sir, good bye")
            exit()

        elif ('your name' in query):
            speak("My name is jarvis, i am a intelligent robot ,made by mihir narkar")

        elif ('open youtube' in query):
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com/")

        elif ('open google' in query):
            speak("Opening google")
            webbrowser.open("https://www.google.com/")

        elif ('show time' in query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")