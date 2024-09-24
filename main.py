from __future__ import print_function

import os
import subprocess
import pygame
import json
import requests
from pyowm import OWM
from geopy import Nominatim
import pyttsx3
from calendar import calendar
import dateparser
import wikipedia
import speech_recognition as sr
import datetime
import os.path
import pyttsx3
import webbrowser
from pyttsx3 import voice
import pyjokes
import pywhatkit
import smtplib
import random
import math
from enum import Enum
from uuid import uuid4
from datetime import date
from randfacts import randfacts
from datetime import datetime
import threading
import time
import tkinter as tk
from win10toast import ToastNotifier
from playsound import playsound
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
#from keras.models import load_model
#from keras.models import Sequential
#from keras.layers import Dense, Activation, Dropout
#from keras.optimizers import SGD
#import tkinter
#from tkinter import *
#import tensorflow as tf
#import pathlib
#import matplotlib.pyplot as plt
#import pandas as pd
#from tensorflow import keras
import deepl

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #gets you the details of the current voice
engine.setProperty('voices', voices[0].id)


#words=[]
#classes = []
#documents = []
#ignore_words = ['?', '!']
#data_file = open('intents.json').read()
#intents = json.loads(data_file)

shoplist=['LList is' , ]




def authentication():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
    except HttpError as error:
        print('An error occurred: %s' % error)

def calender(n, service):
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print(f'Getting the upcoming {n} events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=n, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])



def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.

#if __name__=="__main__" :
    #speak('Hello Mathew, I am Jay, your Artificial intelligence assistant. Please tell me how may I help you')

def fact():
    fun_fact = randfacts.get_fact()
    print(fun_fact)
    speak(fun_fact)



def wishme():
   hour = int(datetime.datetime.now().hour)
   if hour >= 0 and hour < 12:
       speak("GGood Morning!")

   elif hour >= 12 and hour < 18:
       speak("GGood Afternoon!")

   else:
       speak("GGood Evening!")

   speak(' Whats up Mathew, I am Jay, your assistant. How may I help you?')

def greeting():
   hour = int(datetime.now().hour)
   if hour >= 0 and hour < 12:
       speak("GGood Morning!")

   elif hour >= 12 and hour < 18:
       speak("GGood Afternoon!")

   else:
       speak("GGood Evening!")

   speak('MMathew!')

def dutchnews():
    r= requests.get('https://newsapi.org/v2/top-headlines?country=nl&apiKey=edec260df2224d8295c3c32b0459bf7c')
    data = json.loads(r.content)
    #speak(data)
    print('Title: ' + data['articles'][1]['title'])
    print('Description: ' + data['articles'][1]['description'])
    print('Content: ' + data['articles'][1]['content'])
    speak('Title: ' + data['articles'][1]['title'])
    speak('Description: ' + data['articles'][1]['description'])
    speak('Content: ' + data['articles'][1]['content'])
    print('Url: ' + data['articles'][1]['url'])
    speak("Here is more information, the info is in the link")
    speak("SSecond part of the news: ")
    print('Title: ' + data['articles'][2]['title'])
    print('Description: ' + data['articles'][2]['description'])
    print('Content: ' + data['articles'][2]['content'])
    speak('Title: ' + data['articles'][2]['title'])
    speak('Description: ' + data['articles'][2]['description'])
    speak('Content: ' + data['articles'][2]['content'])
    print('Url: ' + data['articles'][2]['url'])
    speak("Here is more information, the info is in the link")

def technews():
    r= requests.get('https://newsapi.org/v2/top-headlines?country=gb&category=technology&apiKey=edec260df2224d8295c3c32b0459bf7c')
    data = json.loads(r.content)
    #speak(data)
    print('Title: ' + data['articles'][2]['title'])
    print('Description: ' + data['articles'][2]['description'])
    print('Content: ' + data['articles'][2]['content'])
    speak('Title: ' + data['articles'][2]['title'])
    speak('Description: ' + data['articles'][2]['description'])
    speak('Content: ' + data['articles'][2]['content'])
    print('Url: ' + data['articles'][2]['url'])
    speak("Here is more information, the info is in the link")
    speak("SSecond part of the news: ")
    print('Title: ' + data['articles'][3]['title'])
    print('Description: ' + data['articles'][3]['description'])
    print('Content: ' + data['articles'][3]['content'])
    speak('Title: ' + data['articles'][3]['title'])
    speak('Description: ' + data['articles'][3]['description'])
    speak('Content: ' + data['articles'][3]['content'])
    print('Url: ' + data['articles'][3]['url'])
    speak("Here is more information, the info is in the link")
def footballnews():
    r= requests.get('https://newsapi.org/v2/top-headlines?country=gb&category=sports&apiKey=edec260df2224d8295c3c32b0459bf7c')
    data = json.loads(r.content)
    #speak(data)
    print('Title: ' + data['articles'][1]['title'])
    print('Description: ' + data['articles'][1]['description'])
    print('Content: ' + data['articles'][1]['content'])
    speak('Title: ' + data['articles'][1]['title'])
    speak('Description: ' + data['articles'][1]['description'])
    speak('Content: ' + data['articles'][1]['content'])
    speak("SSecond part of the news: ")
    print('Title: ' + data['articles'][5]['title'])
    print('Description: ' + data['articles'][5]['description'])
    print('Content: ' + data['articles'][5]['content'])
    speak('Title: ' + data['articles'][5]['title'])
    speak('Description: ' + data['articles'][5]['description'])
    speak('Content: ' + data['articles'][5]['content'])



def addshopping():
    speak("What do you want to add to your list?")
    print("What do you want to add to your list?")
    item=takeCommand()
    item=item.lower()
    shoplist.append(item)
    done = True
    speak(f"I have added {item} to the list!")

def listshopping():
    speak("Here are your shopping items:")
    print("Here are your shopping items:")
    speak(shoplist)
    print(shoplist)


#-------------------------------------------------------------------------------------------------
class Status(Enum):
    """ The Todo Statuses """
    NOT_STARTED = 0
    IN_PROGRESS =  1
    COMPLETED = 2


class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Item():
    __creation_date = date.today()
    __title = "empty"
    __status = Status.NOT_STARTED
    __priority = Priority.LOW
    __flag = False
    __url = ""
    __due_date = date
    __icon = ""
    __state = False
    __notes = ""

    def __init__(self, title:str=None):
        if title is not None:
            self.__title = title
        self.__id = str(uuid4())

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value:str):
        self.__title = value

    @property
    def priority(self):
        return self.__priority.name

    @priority.setter
    def priority(self, value:Priority):
        self.__priority = value

    @property
    def creation_date(self):
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value):
        self.__creation_date = value

    @property
    def age(self):
        return self.__creation_date - date.today()

    @property
    def status(self):
        return self.__status.name
    @status.setter
    def status(self, value:Status):
        self.__status = value

    @property
    def id(self):
        return self.__id

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, value:bool):
        self.__flag = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value:str):
        self.__url = value

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value:date):
        self.__due_date = value

    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, value:str):
        self.__icon = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value:bool):
        self.__state = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value:str):
        self.__value = value

class Todo():
    __todos = []

    def __init__(self):
        print("new todo list created")
        self._current = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < len(self.__todos) -1 :
            self._current += 1
            print(self.__todos[self._current].title)
            return self.__todos[self._current]
        else:
            self._current = -1
        raise StopIteration

    def __len__(self):
        """ Returns the number of items in the Todo List """
        return len(self.__todos)


    def new_item(self, item:Item):
        self.__todos.append(item)

    @property
    def items(self)->list:
        return self.__todos

    def show(self):
        print("*"*80)
        for item in self.__todos:
            print(item.title, item.status, item.priority, item.age)

    @classmethod
    def show(cls):
        print("*"*80)
        print("Todo Items")
        print('*'*80)
        count = 1
        if len(cls.__todos) == 0:
            print("No items in list!")
        else:
            for item in cls.__todos:
                print(count, item.title, item.status, item.priority, item.age, item.id)
                count += 1
            print("")

    def remove_item(self, uuid:str=None, title:str=None)->bool:
        if title is None and uuid is None:
            print("You need to provide some details for me to remote it, either UUID or title")
        if uuid is None and title:
            for item in self.__todos:
                if item.title == title:
                    # del self.__todos[item
                    self.__todos.remove(item)
                    return True
            print("Item with title", title, 'not found')
            return False
        if uuid:
            self.__todos.remove(uuid)
            return True

def add_todo()->bool:
    item = Item()
    speak("Tell me what to add to the list")
    try:
        item.title = takeCommand()
        todo.new_item(item)
        message = "Added" + item.title
        speak(message)
        return True
    except:
        print("oops there was an error")
        return False

def list_todos():
    if len(todo) > 0:
        speak("Here are your to do's")
        for item in todo:
            speak(item.title)
    else:
        speak("The list is empty!")

def remove_todo()->bool:
    speak("Tell me which item to remove")
    try:
        item_title = takeCommand()
        todo.remove_item(title=item_title)
        message = "Removed" + item_title
        speak(message)
        return True
    except:
        print("opps there was an error")
        return False

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
def add_event()->bool:
    speak("WWhat is the name of the event")
    event_name = takeCommand()
    speak("WWhen is this event?")
    event_begin = takeCommand()
    event_isodate = dateparser.parse(event_begin).strftime("%Y-%m-%d %H")#:%M:%S
    speak("WWhat is the event description?")
    event_description = takeCommand()
    message = "OOk, adding event" + event_name
    speak(message)
    calendar.add_event(begin=event_isodate, name=event_name, description=event_description)
    calendar.save()

def remove_event()->bool:
    speak("What is the name of the event you want to remove?")
    try:
        event_name = takeCommand()
        try:
            calendar.remove_event(event_name=event_name)
            speak("Event removed successfully")
            calendar.save()
            return True
        except:
            speak("Sorry I could not find the event",event_name)
            return False
    except:
        print("opps there was an error")
        return False

def list_events(period):
    this_period = calendar.list_events(period=period)
    if this_period is not None:
        message = "There "
        if len(this_period) > 1:
            message = message + 'are '
        else:
            message = message + 'is '
        message = message + str(len(this_period))
        if len(this_period) > 1:
            message = message + ' events'
        else:
            message = message + ' event'
        print(message)
        speak(message)
        for event in this_period:
            # alf.say(event.begin.datetime)
            event_date = event.begin.datetime
            weekday = datetime.strftime(event_date, "%A")

            print(weekday, type(weekday))
            day = str(event.begin.datetime.day)
            month = datetime.strftime(event_date, "%B")
            year = datetime.strftime(event_date, "%Y")
            message = "On " + weekday + " " + day + " of " + month + " " + year
            print(message)
            speak(message)
            name = event.name
            print("name is:",name)
            message = "there is an event called " + name
            speak(message)
            description = event.description
            message = "the event description is " + description
            print("description is:",description)
            speak(message)
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
class Weather():
    # The location of where you want the weather forecast for
    __location = 'Uithoorn, NL'

    # Replace this with your own API key
    api_key = '9c20b5a5c8dffdfe081ae71896436de3'

    def __init__(self):
        self.ow = OWM(self.api_key)
        self.mgr = self.ow.weather_manager()
        locator = Nominatim(user_agent="myGeocoder")
        city = "Uithoorn"
        country = "Netherlands"
        self.__location = city + ' ' + country
        loc = locator.geocode(self.__location)
        self.lat = loc.latitude
        self.long = loc.longitude

    def uv_index(self, uvi: float):
        """ Returns a message depending on the UV Index provided """
        message = ""
        if uvi <= 2.0:
            message = "The Ultra Violet level is low, no protection required."
        if uvi >= 3.0 and uvi < 6.0:
            message = "The Ultra Violet level is medium, skin protection is required."
        if uvi >= 6.0 and uvi < 8.0:
            message = "The Ultra Violet level is high, skin protection is required."
        if uvi >= 8.0 and uvi < 11.0:
            message = "The Ultra Violet level is very high, extra skin protection is required."
        if uvi >= 11.0:
            message = "The Ultra Violet level is extemely high, caution is adviced and extra skin protection is required."
        return message

    @property
    def weather(self):
        """ Returns the current weather at this location """
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        return forecast

    @property
    def forecast(self):
        """ Returns the forecast at this location

        AI will say:

        Today will be mostly <detailed_status>, with a temperature of , and it will feel like <feels_like>, humidity is, and pressure is
        sunrise is at , and sunset is at
        Tomorrow

        """
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        detailed_status = forecast.forecast_daily[0].detailed_status
        pressure = str(forecast.forecast_daily[0].pressure.get('press'))
        humidity = str(forecast.forecast_daily[0].humidity)
        # print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        sunrise = datetime.utcfromtimestamp(forecast.forecast_daily[0].sunrise_time()).strftime('%H:%M:%S')
        temperature = str(forecast.forecast_daily[0].temperature('celsius').get('day'))
        temp_high = str(forecast.forecast_daily[0].temperature('celsius').get('temp_min'))
        temp_low = str(forecast.forecast_daily[0].temperature('celsius').get('temp_max'))
        sunset = datetime.utcfromtimestamp(forecast.forecast_daily[0].sunset_time()).strftime('%H:%M:%S')
        feels_like = str(forecast.forecast_daily[0].temperature('celsius').get('feels_like_day'))
        uvi = forecast.forecast_daily[0].uvi

        # print('detailed status:',detailed_status)
        # print('humidity',humidity)
        print('temperature', temperature)
        # print('sunrise',sunrise)
        # print('sunset',sunset)
        # print('feels_like',feels_like)
        # print('pressure',pressure)
        print("UVI: ", uvi)

        # + ", with a high of " + temp_high + " and a low of " + temp_low \

        message = "Here is the Weather: Today will be mostly " + detailed_status \
                  + ", with a temperature of  " + temperature \
                  + ", humidity of " + humidity + " percent" \
                  + " and a pressure of " + pressure + " millibars" \
                  + ". Sunrise was at " + sunrise \
                  + ", and Sunset at " + sunset \
                  + ". " + self.uv_index(float(uvi))
        return message

    @property
    def location(self):
        """ Returns the currently set location """
        return self.__location

    @location.setter
    def location(self, value):
        """ Sets the current location """
        self.__location = value
#-------------------------------------------------------------------------------------------------
def note(text):
    date = datetime.now()
    filename = str(date).replace(":", "-") + "-note.txt"
    with open(filename, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", filename])

def getaudio():
    e = sr.Recognizer()
    with sr.Microphone() as source:
        audio = e.listen(source)
        said=""

        try:
            said= e.recognize_google(audio)
            print (said)
        except Exception as l:
            print("Exception: " + str(l))


def takeCommand():
    #It takes microphone input from the user and returns string output
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
         try:
             print("Recognizing...")
             query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
             print(f"You said: {query}\n")   # User query will be printed.
         except Exception as e:
             # print(e)  use only if you want to print the error!
             speak("Say that again please...")  # Say that again will be printed in case of improper voice
             print("Say that again please...")
             return "None"  # None string will be returned
         return query

def joke():
    funny= pyjokes.get_joke()
    print (funny)
    speak(funny)

if __name__ == "__main__":
    wake="hey dude"
    while True:

        query = takeCommand().lower() #Converting user query into lower case
        # Logic for executing tasks based on query
        if "hi" in query:
            greeting()
        elif 'hello' in query:
            greeting()
        elif 'who are you' in query:
            speak("I am Jay, a virtual assistant made by programmer Mathew, how can i help you?")
            print("I am Jay, a virtual assistant made by programmer Mathew, how can i help you?")
            takeCommand()
        elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            print(f"MMMathew, the time is {strTime}")
            speak(f"MMMathew, the time is {strTime}")
        elif 'open chrome' in query:
            Google = "C:\Program Files\Google\Chrome\Application\chrome.exe"  # that's the code path.
            os.startfile(Google)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'play music' in query:
            Spotify = ''
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'formula 1 schedule' in query:
            webbrowser.open('https://www.formula1.com/en/racing/2021.html')
        elif 'formula one schedule' in query:
            webbrowser.open('https://www.formula1.com/en/racing/2021.html')
        elif 'open formula 1' in query:
            webbrowser.open('https://www.formula1.com/')
        elif 'bye' in query:
            speak("OOkay! Have a great day!")
            exit(1)
        elif 'open managebac' in query:
            webbrowser.open('https://aics.managebac.com/student')
        elif 'play music' in query:
            webbrowser.open("https://open.spotify.com/")
        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com/')
        elif 'a joke' in query:
            joke()
        elif 'how are you' in query:
            speak("I am doing good thank you! How about you?")
            print("I am doing good thank you! How about you?")
        elif 'i am good' in query:
            print("That is great! I am glad to hear.")
            speak("That is great! I am glad to hear.")
        elif 'i feel bad' in query:
            print("Oh! That is bad. Will a joke cheer you up?")
            speak("Oh! That is bad. Will a joke cheer you up?")
        elif 'yes that would make me better' in query:
            joke()
        elif 'no thank you' in query:
            print("Ok. I hope you feel better later! Should I leave or should I stay?")
            speak("Ok. I hope you feel better later! Should I leave or should I stay?")
        elif "you can stay" in query:
            print("Ok!")
            speak("Ok!")
        elif "i feel better alone" in query:
            exit(1)
        elif 'play a game' in query:
            print("Which game do you want? Space Shooters or Ping pong?")
            speak("Which game do you want? Space Shooters, Ping pong or Rock Paper Scicors?")
        elif 'space shooters' in query:
            speak("Ok! Here is space shooters.")
            width = 555
            height = 1002
            fps = 30
            white = (255, 255, 255)
            yellow = (255, 255, 0)
            black = (0, 0, 0)
            pygame.init()
            pygame.mixer.init()
            display = pygame.display.set_mode((width, height))
            pygame.display.set_caption("Galaxy Shooter")
            clock = pygame.time.Clock()
            spaceship = pygame.image.load("C:/Users/mathe/OneDrive/Documents/spaceship.png")
            background = pygame.image.load("C:/Users/mathe/Videos/Captures/s.jpg")
            Meteor = pygame.image.load("C:/Users/mathe/OneDrive/Documents/rock.png")


            def mob(mobx, moby):
                display.blit(Meteor, (mobx, moby))


            def message(text):
                text1 = pygame.font.Font('freesansbold.ttf', 20)
                text2 = text1.render(text, True, yellow)
                text3 = text2.get_rect()
                text3.center = ((width / 2), (height / 2))
                display.blit(text2, text3)
                pygame.display.update()
                time.sleep(2)


            def score(count):
                num1 = pygame.font.Font('freesansbold.ttf', 15)
                num2 = num1.render("Score:" + str(count), True, yellow)
                display.blit(num2, (0, 0))


            def crash():
                message("Oh no you have crashed!")
                pygame.quit()


            def gameloop():
                x = width / 2
                y = 900
                dodge = 0
                mob_startx = random.randrange(0, width)
                mob_starty = -200
                mob_speed = 15
                mob_height = 43
                mob_width = 43
                spaceshipwidth = 99
                k = True
                while k:
                    x_change = 0
                    clock.tick(fps)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            k = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                x_change = 20
                            elif event.key == pygame.K_LEFT:
                                x_change = -20
                    x = x + x_change
                    display.blit(background, (0, 0))
                    mob(mob_startx, mob_starty)
                    mob_starty = mob_starty + mob_speed
                    display.blit(spaceship, (x, y))
                    score(dodge)
                    if mob_starty > height:
                        mob_starty = -50
                        mob_startx = random.randrange(0, width)
                        dodge = dodge + 1
                    if y < mob_starty + mob_height - 15:
                        if x > mob_startx - 15 and x < mob_startx + mob_width - 15 or x + spaceshipwidth > mob_startx - 15 and x + spaceshipwidth < mob_startx + mob_width - 15:
                            crash()
                    pygame.display.update()


            gameloop()
            pygame.quit()
        elif 'ping pong' in query:
            speak("Ok! here is ping pong.")
        elif 'rock paper scissors' in query:
            choice= random.choice(['Rock','Paper','Scissors'])
            speak("Ready?")
            speak("Rock.... Paper .... Scissors... SHOOT!")
            print (choice)
            speak("II chose......"+choice)
        elif 'open davinci' in query:
            Davinci = "C:\Program Files\Blackmagic Design\DaVinci Resolve\Resolve.exe"
            os.startfile(Davinci)
        elif 'gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/")
        elif 'coding dashboard' in query:
            webbrowser.open('https://hellolearner.com/dashboard')
        elif 'play' in query:
            song =query.replace('play','')
            speak('playing' + song)
            pywhatkit.playonyt(song)
        elif 'who is' in query:
            person = query.replace('who is','')
            info = wikipedia.summary(person, 1)
            print (info)
            speak (info)
        elif 'what is' in query:
            thing = query.replace('what is','')
            info = wikipedia.summary(thing, 1)
            print (info)
            speak (info)
        elif 'thank you' in query:
            print("You are welcome!")
            speak("YYou are welcome!")
        elif 'search in google' in query:
            speak("What do you want to search")
            thesearch = takeCommand()
            url = 'https://google.com/search?q=' + thesearch
            webbrowser.get().open(url)
            print("Here is what I found in google")
            speak("Here is what I found in google")
        elif 'search in youtube' in query:
            search = speak("What do you want to search")
            thesearch = takeCommand()
            url = 'https://youtube.com/search?q=' + thesearch
            webbrowser.get().open(url)
            print("Here is what I found in youtube")
            speak("Here is what I found in youtube")
        elif 'date today' in query:
            datetd = datetime.now()
            print(datetd)
            speak(datetd)
        elif "calendar" in query:
            authentication()
            calender(2)
        elif 'note' in query:
            speak("What do you want me to write down?")
            notetext= takeCommand().lower()
            note(notetext)
            speak ("I have made a note of that")
        elif 'fun fact' in query:
            fact()
        elif 'good' in query:
            hour = int(datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("GGood Morning Mathew!")
                speak("HHere is a fact")
                fact()

            elif hour >= 12 and hour < 18:
                speak("GGood Afternoon Mathew!")
                speak("HHere is a joke")
                joke()
                speak("HHere is a fact also")
                fact()

            else:
                speak("GGood Night Mathew!")
                speak("HHave a great evening and a great sleep")
        elif 'add event' in query:
            add_event()
        elif 'remove event' in query:
            remove_event()
        elif "my events" in query:
            list_events()
        elif 'weather' in query:
            myweather= Weather()
            print(myweather.forecast)
            speak(myweather.forecast)
        elif 'add todo' in query:
            add_todo()
        elif 'remove item' in query:
            remove_todo()
        elif 'my todos' in query:
            list_todos()
        elif 'dutch news' in query:
            dutchnews()
        elif 'Dutch news' in query:
            dutchnews()
        elif 'tech news' in query:
            technews()
        elif 'Tech news' in query:
            technews()
        elif 'football news' in query:
            footballnews()
        elif 'Football news' in query:
            footballnews()
        elif 'date tomorrow' in query:
            datetm=datetime.now()+1
            print(datetm)
            speak(datetm)
        elif 'add item' in query:
            addshopping()
        elif 'my shopping items' in query:
            listshopping()
        elif 'translate to dutch' in query:
            speak("What do you want to translate?")
            print("What do you want to translate?")
            eword = takeCommand()
            searchh = "https://translate.google.com/?sl=en&tl=nl&text=" + eword + "&op=translate"
            webbrowser.get().open(searchh)
            print("Here is the translation")
            speak("Here is the translation")
        elif 'open school loadout' in query:
            webbrowser.open('https://aics.managebac.com/student')
            webbrowser.open('https://mail.google.com/mail/u/1/#inbox')
            webbrowser.open('https://drive.google.com/drive/u/1/my-drive')
            webbrowser.open('https://classroom.google.com/u/1/h')
        elif 'open Google Earth' in query:
            GoogleEarth = "C:\Program Files\Google\Google Earth Pro\client\googleearth.exe"
            os.startfile(GoogleEarth)
        #elif 'translate' in query:


        #The sum part is not correct, whenever free just research into this in the youtube channel that I look or somewhere else
        #https://newsapi.org/s/google-news-api <- This link is for Google News and it can get news from many diffrent places, once you are free try to set it up



                
#a=math.sqrt(64)
#print(a)
#b=math.pow(23,2)
#print(b)
#c=math.floor(9.1234556677)
#print(c)
#d=math.ceil(9.112233456677)
#print(d)
