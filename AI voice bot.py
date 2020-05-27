import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.25)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Please say something")


def take_command():  # takes user input from microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Please say that again.")
        speak("Please say that again")
        query = 'none'
    return query

query = take_command()