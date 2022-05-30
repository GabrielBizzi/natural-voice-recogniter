import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord, open_shell
from random import choice
from utils import opening_text
from pprint import pprint


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    print(hour)
    if (hour >= 6) and (hour < 12):
        print(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        print(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        print(f"Good Evening {USERNAME}")
    print(f"I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            print(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                print("Good night sir, take care!")
            else:
                print('Have a good day sir!')
            exit()
    except Exception:
        print('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notes' in query:
            open_notepad()

        elif 'open disc' in query:
            open_discord()

        elif 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calc' in query:
            open_calculator()
        
        elif 'open shell' in query:
            open_shell()

        elif 'ip address' in query or 'what is my ip' in query or 'my ip' in query:
            ip_address = find_my_ip()
            print(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query or 'search in wikipedia' in query:
            print('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            print(f"According to Wikipedia, {results}")
            print("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query or 'play on youtube' in query:
            print('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query or 'google' in query:
            print('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            print(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            print("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            print("I've sent the message sir.")

        elif "send an email" in query:
            print("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            print("What should be the subject sir?")
            subject = take_user_input().capitalize()
            print("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                print("I've sent the email sir.")
            else:
                print("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            print(f"Hope you like this one sir")
            joke = get_random_joke()
            print(joke)
            print("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            print(f"Here's an advice for you, sir")
            advice = get_random_advice()
            print(advice)
            print("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query:
            print(f"Some of the trending movies are: {get_trending_movies()}")
            print("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            print(f"I'm reading out the latest news headlines, sir")
            print(get_latest_news())
            print("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            print(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            print(f"The current temperature is {temperature}, but it feels like {feels_like}")
            print(f"Also, the weather report talks about {weather}")
            print("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")