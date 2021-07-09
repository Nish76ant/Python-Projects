"""
What can this A.I. assistant do for you?
It can send emails for you.
It can play music for you.
It can do Wikipedia searches for you.
It is capable of opening websites like Google, Youtube, etc., in a web browser.
It is capable of opening your code editor or IDE with a single voice command.
Enough talk! Let's start building our own Assistant....

1 – Starting VS Code. 
Start a new project and make a file called jarvis.py.

2 – Defining Speak Function
The and first and foremost thing for an A.I. assistant is that it should be able to speak. To make our J.A.R.V.I.S. 
talk, we will make a function called speak().
 This function will take audio as an argument, and then, it will pronounce it.
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time

engine = pyttsx3.init() #Intialize the your
voices = engine.getProperty('voices')
# print(voices[1].id) #david voice
# What Is VoiceId?
# Voice id helps us to select different voices.
# voice[0].id = Male voice 
# voice[1].id = Female voice
engine.setProperty('voice', voices[0].id)



# We made a function called speak() at the starting of this tutorial. Now,
# we will write our speak() function so that it can convert our text to speech.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Nishant')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Nishant')
    else:
        speak('Good Evening Nishant')
    speak('I am your Assistant Nishant...How may I help you ?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='eng-us')
        print(f"You said {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again Please....")
        return 'None'
    return query

# def sendEmail(to,content):
#     server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#     server.ehlo()
#     server.login('sender','your_gmail_paasword')
#     server.sendmail('sender_mail','reciver_',content)
#     server.close()
    
if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "D:\\Webtek Labs Delhi Data Science Program Daily Practice Set\\Nishant"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open chrome' in query:
            codepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)

        elif 'email to nishant' in query:
            speak('What should i say ?')
            content = takeCommand()
            server = smtplib.SMTP_SSL('smtp.gmail.com',465)
            server.ehlo()
            server.login('sender_email','email_password')
            server.sendmail('sender_email','reciver_email',content)
            speak('Email has been sent')
            server.close()


            # try:
            #     speak('What should i say ?')
            #     content = takeCommand()
            #     to = "kumarkeshav32338@gmail.com"   
            #     sendEmail(to,content) 
            #     speak("Email has been sent !")

            # except Exception as e:
            #     print(e)
            #     speak("Sorry my frinend Nishant i am not able to send this email..")
