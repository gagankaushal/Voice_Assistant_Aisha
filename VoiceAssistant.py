from gtts import gTTS
import playsound
import speech_recognition as sr
import os
# import sys
import re
# import dbus
# import dbus.glib
# import dbus.service
# import gobject


from datetime import datetime, timedelta
import webbrowser
# from xdo import Xdo
from selenium import webdriver
# import smtplib
# import requests
# import subprocess
# from pyowm import OWM
# import youtube_dl
# import vlc
# import urllib
import urllib.request as urllib2
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
    elif 'play' in command:
        # elif 'play me a song' in command:
                    sofiaResponse('What song shall I play Gagan?')
                    mysong = myCommand()
        # elif 'play me a song' in command:
            # mysong = myCommand()
                    # if mysong:
                    flag = 0
                    url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup1 = soup(html,"lxml")
                    url_list = []
                    for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
                            if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                                    flag = 1
                                    final_url = 'https://www.youtube.com' + vid['href']
                                    url_list.append(final_url)
                                    # webbrowser.open(final_url)
                                    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
                                    driver.get(final_url)
                                    driver.execute_script(
                                    'document.getElementsByTagName("video")[0].paused ?'
                                    'document.getElementsByTagName("video")[0].play() :'
                                    'document.getElementsByTagName("video")[0].pause();')
                                    elem = driver.find_element_by_class_name('ytp-play-button')
                                    # WebDriverWait(driver, 30).until(elem)
                                    elem.click()
                                    sofiaResponse('Enjoy the song, Gagan!')
                                    break

    elif 'pause' in command:
        # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        elem = driver.find_element_by_class_name('ytp-play-button')
        elem.click()
        sofiaResponse('Video has been paused!')

    elif 'resume' in command:
        elem = driver.find_element_by_class_name('ytp-play-button')
        elem.click()
        sofiaResponse('Video has been resumed!')


    # url = url_list[0]
    #             ydl_opts = {}
    # os.chdir(path)
    #             with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #                 ydl.download([url])
    #             vlc.play(path)
    # if flag == 0:
    #                 sofiaResponse('I have not found anything in Youtube ')


def youtubePause():

    # xdo = Xdo()
    # win_id = xdo.select_window_with_click()
    # Using Chrome to access web
    driver = webdriver.Chrome()

# def main():
#     """Open youtube and start dbus listener."""
#     global browser

#     # loop = gobject.MainLoop()

#     # bus = dbus.SessionBus()
#     # bus_name = dbus.service.BusName('org.mpris.MediaPlayer2.youtube', bus=bus)

#     # MediaPlayer2(bus_name, '/org/mpris/MediaPlayer2', loop)

#     browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#     browser.get('https://youtube.com')

#     # loop.run()


# class MediaPlayer2(dbus.service.Object):
#     # def __init__(self, bus_name, object_path, loop):
#     #     dbus.service.Object.__init__(self, bus_name, object_path)
#     #     self.loop = loop

#     @dbus.service.method('org.mpris.MediaPlayer2.Player')
#     def Previous(self):
#         global browser, last_previous
#         print('Received previous signal')
#         now = datetime.now()
#         if now - last_previous < timedelta(seconds=5):
#             browser.back()
#         else:
#             elem = browser.find_element_by_tag_name('video')
#             elem.send_keys('0')
#         last_previous = now

#     @dbus.service.method('org.mpris.MediaPlayer2.Player')
#     def PlayPause(self):
#         global browser
#         print('Received PlayPause signal')
#         browser.execute_script(
#             'document.getElementsByTagName("video")[0].paused ?'
#             'document.getElementsByTagName("video")[0].play() :'
#             'document.getElementsByTagName("video")[0].pause();')
#         #elem = browser.find_element_by_class_name('ytp-play-button')
#         #elem.click()

#     @dbus.service.method('org.mpris.MediaPlayer2.Player')
#     def Next(self):
#         global browser
#         print('Received next signal')
#         next_video_url = _find_next_video_url(browser)
#         if next_video_url:
#             browser.get(next_video_url)
#         else:
#             browser.forward()


# def _find_next_video_url(c):
#     """Try different ways to determine the url of the next video."""
#     try:
#         next_video_url = sorted(Counter(
#             a.get_property('href')
#             for a in c.find_elements_by_tag_name('a')
#             if a.get_property('href').find('/watch?') >= 0
#         ).items(), key=lambda k: k[1], reverse=True)[0][0]
#     except Exception:
#         pass
#     if next_video_url:
#         return next_video_url
#     next_video_url = browser.find_element_by_class_name('watch-sidebar-body') \
#         .find_element_by_tag_name('a').get_property('href')
#     if next_video_url:
#         return next_video_url

# browser = None
# last_previous = datetime.now()

# if __name__ == '__main__':
#     main()

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

sofiaResponse('Hi Gagan, this is Aisha and I am your personal voice assistant. How can I help you today?')# Please give a command or say "help me" and I will tell you what all I can do for you.'how can I help you today?')

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

while True:
    assistant(myCommand())
# assistant(myCommand())
