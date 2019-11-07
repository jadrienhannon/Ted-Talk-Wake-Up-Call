# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 13:56:49 2019

@author: jadri
"""
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import os
import requests
import random
import volumeControl

os.system("TASKKILL /F /IM Spotify.exe")

videolist = [] # creates list of all videos on page
vidIndex = random.randrange(0, 29, 1)
genre = random.randrange(0,4,1) # index value for list of genres

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
base = "https://www.ted.com/search?cat=videos&q=" # base linked site
queryString = ['tech', 'engineering', 'software', 'space', 'computers'] # possible genres

r = requests.get(base+queryString[genre]) #query for search string

page = r.text
soup = bs(page, 'html.parser') # extract html of search results page

while len(videolist) < vidIndex:
    vids = soup.findAll('a', attrs={'class':'ga-link visible-url-link'}) # finds all links to videos
    
    for v in vids:
        temp = 'https://www.ted.com' + v['href'] # create link to video
        videolist.append(temp) # append each video

video = videolist[vidIndex] # select the most recent video on subject

driver.get(video) # play video
driver.maximize_window() # maximize window
button = driver.find_element_by_id('ted-player') # find play button
button.click() # press play

volumeControl.set_volume(10)