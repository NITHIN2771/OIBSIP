import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def search_web(query):
    webbrowser.open('https://www.google.com/search?q=' + query)

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("Command: " + command)
            return command
        except sr.UnknownValueError:
            print("sorry I could not understand your command.")
            return None
while True:
    command = get_command().lower()

    if "hello dell" in command or "hey dell" in command:
        text_to_speech("Hello! How can I help you?")
    elif "time" in command or "what is the time now" in command:
        text_to_speech(datetime.datetime.now().strftime("%I %M:%p"))
    elif "date" in command or "what is today's date" in command:
        text_to_speech(datetime.datetime.now().strftime("%d/%m/%Y"))
    elif command.startswith("search" or "hey dell search for "):
        query = command[7:]
        search_web(query)
        text_to_speech("Searching for " + query)
    elif "quit" in command or "ok bye" in command or "bye" in command:
        text_to_speech("bye Have a nice day.")
        break
    else:
        text_to_speech("i couldn't get you would you say it again.")
