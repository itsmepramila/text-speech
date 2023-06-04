from winreg import QueryInfoKey
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishME():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I Am Jarvis Sir. Please Tell Me Madam How May I Help You")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


def sendEmail(do, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("chaudharyparmila75@gmail.com", "####****")
    server.sendmail("chaudharyparmila75@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishME()
    while True:
        # if 1:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wekipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "C:\\Users\\Oxford Computer\\Music\\Sunn_Zara_-_Official_Video___JalRaj___Shivin_Narang___Tejasswi_Prakash___Anm.mp3"
            os.startfile(music_dir)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Madam, the time is {strTime}")

        elif "open code" in query:
            CodePath = "C:\\Users\\Oxford Computer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(CodePath)

        elif "email to riya" in query:
            try:
                speak("What Should I Say?")
                content = takeCommand()
                to = "riyabhatta123@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my sister. I am not able to send this email at the moment")
