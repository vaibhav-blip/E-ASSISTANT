import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voices", voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>12:
        speak("good morning sir, i am your assistance")

    elif hour==12 and hour<18:
        speak("good afternoon sir, i am your assistance")

    else:
        speak("good evening sir, i am your assistance")

    speak("hello vaibhav , how may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("wait i am listing...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("loading....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:

        print(e)

        print("say that again please")
        return "None"
    return query


if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dic = "E:\\songs\\music"
            song = os.listdir(music_dic)
            print(song)
            os.startfile(os.path.join(music_dic, song[0]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif "who are you" in query:
            speak("i am v. n, i am developed by vaibhav on sixteen october 2020")

        elif "open program" in query:
            code = "C:\\pycharm\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(code)


        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

















