from gtts import gTTS
import playsound
import speech_recognition as sr
import os
# import sys
import re
import webbrowser
# import smtplib
# import requests
# import subprocess
# from pyowm import OWM
# import youtube_dl
# import vlc
# import urllib
import urllib3
# import json
from bs4 import BeautifulSoup as soup
# from urllib2 import urlopen
# import wikipedia
# import random
# from time import strftime

def myCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print('Say something...')
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
        try:
                command = r.recognize_google(audio).lower()
                print('You said: ' + command + '\n')
        #loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
                print('....')
                command = myCommand();
        return command


# def sofiaResponse(audio):
#     print(audio)
#     for line in audio.splitlines():
#         os.system("say " + audio)

def assistant(command):
    if 'open' in command:
                    reg_ex = re.search('open (.+)', command)
                    if reg_ex:
                            domain = reg_ex.group(1)
                            print(domain)
                            url = 'https://www.' + domain
                            webbrowser.open(url)
                            sofiaResponse('The website you have requested has been opened for you Gagan.')
                    else:
                            pass
    elif 'play a song' in command:
        # elif 'play me a song' in command:
                    mysong = myCommand()
        # elif 'play me a song' in command:
            # mysong = myCommand()
                    if mysong:
                            flag = 0
                            url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                            response = urllib3.urlopen(url)
                            html = response.read()
                            soup1 = soup(html,"lxml")
                            url_list = []
                            for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
                                    if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                                            flag = 1
                                            final_url = 'https://www.youtube.com' + vid['href']
                                            url_list.append(final_url)
    # url = url_list[0]
    #             ydl_opts = {}
    # os.chdir(path)
    #             with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #                 ydl.download([url])
    #             vlc.play(path)
    # if flag == 0:
    #                 sofiaResponse('I have not found anything in Youtube ')

num = 1

def sofiaResponse(output): 
        global num 
    
        # num to rename every audio file  
        # with different name to remove ambiguity 
        num += 1
        print("Aisha : ", output) 
    
        toSpeak = gTTS(text = output, lang ='en', slow = False) 
        # saving the audio file given by google text to speech 
        # file = str(num)+".mp3
        file = str(num)+".mp3"  
        toSpeak.save(file)
            
        # playsound package is used to play the same file. 
        playsound.playsound(file, True)  
        os.remove(file)

while True:
    sofiaResponse('Hi Gagan, how can I help you today?')
    assistant(myCommand())
# assistant(myCommand())
