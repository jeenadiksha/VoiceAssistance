import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voices",voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 4 and hour <= 12):
        speak("Good Morning")

    elif(hour >= 12 and hour <= 4):
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("I am jarvis . Please tell me how may I help you")

def takeCommand():
    "It takes microphone input from the user and returns string output"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio,Language = "en - in")
        print(f"User said: {query}\n")



    except Exception as e:
        print("Say that again please ...")
        return "None"        
    return query


wishMe()    
takeCommand()
speak()


