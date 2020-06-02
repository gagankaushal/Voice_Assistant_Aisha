from gtts import gTTS
import playsound
import speech_recognition as sr
import os
import re
from datetime import datetime, timedelta
import webbrowser
from selenium import webdriver
import urllib.request as urllib2
from bs4 import BeautifulSoup as soup

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


def youtubePause():

    # xdo = Xdo()
    # win_id = xdo.select_window_with_click()
    # Using Chrome to access web
    driver = webdriver.Chrome()


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
