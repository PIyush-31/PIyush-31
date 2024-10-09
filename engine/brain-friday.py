import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import smtplib 
from email.message import EmailMessage
import random
import pyautogui
import time
import json 
import wolframalpha
import pyjokes
client = wolframalpha.Client('RQ66EK-PRVJYQPRGW')
import pywhatkit
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import PyPDF2
from transformers import pipeline 
from chat import*
import wave 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# Initialize Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='0',
                                               client_secret='0',
                                               redirect_uri='https://fri-spotify/callback',
                                               scope='user-library-read user-modify-playback-state'))

recognizer = sr.Recognizer()


NEWS_API_KEY = ('0')


def get_latest_news():
    news_headlines = []
    res = requests.get(
    f"https://newsapi.org/v2/top-headlines?country=in&apiKey={'0'}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def play_spotify_song(song_name):
    results = sp.search(q=song_name, type='track')
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][1]['uri']
        sp.start_playback(uris=[track_uri])
    else:
        speak(f"Sorry, I couldn't find the song '{song_name}' on Spotify.")

def open_notepad():
    os.startfile(['notepad'])

def open_cmd():
    os.system('start cmd')


def transcribe_audio(audio_data, model_name, api_token):
    """Transcribes audio data using a Hugging Face model and API.

    Args:
        audio_data: The audio data to be transcribed (assumed to be in WAV format).
        model_name: The name of the Hugging Face model to use.
        api_token: Your Hugging Face API token.

    Returns:
        The transcription of the audio data.
    """

    with wave.open(audio_data, 'rb') as wav_file:
        # Get frame rate and number of frames
        frame_rate = wav_file.getframerate()
        frames = wav_file.getnframes()
        # Extract raw audio bytes
        audio_bytes = wav_file.readframes(frames)

    # Convert raw bytes to a list (required by Hugging Face API)
    audio_list = list(audio_bytes)

    url = "https://api-inference.huggingface.co/models/" + 'meta-llama/Meta-Llama-3.1-70B-Instruc'
    headers = {"Authorization": f"Bearer {'0'}"}
    data = {"inputs": audio_list}  # Use a list instead of raw bytes

    try:
        response = requests.post(url, headers=headers, json=data)
        transcription = response.json()[0]["text"]
        return transcription
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

def pdf_reader(self):
    self.talk("Boss enter the name of the book which you want to read")
    n = input("Enter the book name: ")
    n = n.strip()+".pdf"
    book_n = open(n,'rb')
    pdfReader = PyPDF2.PdfFileReader(book_n)
    pages = pdfReader.numPages
    self.talk(f"Boss there are total of {pages} in this book")
    self.talk("plsase enter the page number Which I nedd to read")
    num = int(input("Enter the page number: "))
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)
    self.talk(text)

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("friday","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,5)
            speak(result)

        except:
            speak("No speakable output available")

def play_on_youtube(video):
    kit.playonyt(video)


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login("piyushmisal25@gmail.com",'enter your mail password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def computational_intelligence(question):
    try:
        client = wolframalpha.Client('RQ66EK-PRVJYQPRGW')
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry boss there is some problem here we will check soon")
        return None

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon !")   

    else:
        speak("Good Evening !")  

    speak("I am friday, the AI virtual assistant created by Piyush")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)    
        print("Say that again please...")
        query = 'Nothing'
        return ""
    return query
    
a = 1
if a==1:
    print(wishMe())
    while True :
        print("to activate please tell the password")
        speak("to activate please tell the password")
        query = takeCommand().lower()
        if '3311' in query:
            print("verified")
            speak("verified")
            print("Welcome back boss good to see you back, what's on your mind")
            speak("Welcome back boss good to see you back, what's on your mind")
            
    
            while True:
            
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=5)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    
                elif 'open youtube' in query:
                    webbrowser.open("https//www.youtube.com")
                
                elif "calculate" in query:
                 question = query
                 answer = computational_intelligence(question)
                 speak(answer)
            
                elif "what is" in query or "who is" in query:
                  question = query
                  answer = computational_intelligence(question)
                  speak(answer)

                if "joke" in query:
                 joke = pyjokes.get_joke()
                 print(joke)
                 speak(joke)
                
                elif 'youtube' in query:
                   speak("boss what's on your mind")
                   video = takeCommand().lower()
                   play_on_youtube(video)
                   
                
                elif 'search google for' in query:
                    searchGoogle(query)
                   
                
                elif 'latest news' in query:
                    speak(f"I'm reading out the latest news headlines, sir")
                    speak(get_latest_news())
                    speak("For your convenience, I am printing it on the screen sir.")
                    print(*get_latest_news(), sep='\n')

                elif 'open google' in query:
                    webbrowser.open("https://www.google.com")
                
                elif 'play a song' in query:
                    music = "D:\\Aashiqui 2 songs"
                    song = os.listdir(music)
                    s = random.randint(0,10)
                    os.startfile(os.path.join(music,song[s]))

                elif "play song on Spotify" in query:
                 speak("Sure, what's the name of the song you'd like to play?")
                 with sr.Microphone() as song_source:
                    audio = recognizer.listen(song_source)
                    song_name = recognizer.recognize_google(audio).lower()
                 play_spotify_song(song_name)
          
                elif 'send an email' in query:
                    email_list = {'first mail':"piyushmisal25@gmail.com",'second mail':"enter someone mail ID"}
                    speak("ok sir     to whom you want to sent the email")
                     
                    name = takeCommand().lower()
                    receiver = email_list.get(name,'')
                
                    if receiver:
                        speak("What's the subject of the email?")
                        subject = takeCommand()
                        speak("What's the content of the email?")
                        message = takeCommand()
                        send_email(receiver, subject, message)
                        speak("Email sent successfully")
                   
                elif 'open notepad' in query:
                    speak("Opening Notepad")
                    os.system('notepad.exe')

                elif 'open cmd' in query:
                    speak("Opening Command Prompt")
                    open_cmd()

                elif query == 'Friday see you soon' or query == 'Friday i will talk to you later':
                      print("Ok boss, waiting for next conversion with you")
                      speak("Ok boss, waiting for next conversion with you")
                      break
                
                elif 'read Bhagavad Gita Sloka'in query:
                    speak("sure you have a bhagavad gita shloka")
                    speak("Karmaṇye  vādhikāraste mā phaleṣhu kadācana mā karmaphala hetur bhūrmā te saṅgo stva karmaṇi")
                
                elif 'tell my favourite quote from Dark Knight' in query:
                    speak("Here is your favourite quote from the Dark Knight")
                    speak("why do we fall sir, so that we can learn to pick ourselves up")
            
                elif 'what is your name' in query:
                    speak("My name is Friday, the AI virtual assistant created by Piyush")

                elif 'open the calculator file from github' in query:
                 webbrowser.open("https://github.com/ine-rmotr-projects/itp-simple-calculator.git")
                 speak("The calculator file has been opened in your browser")

                elif ("read PDF" in query) or ("pdf" in query):
                 query=(pdf_reader)
               
               
                