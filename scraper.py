from bs4 import BeautifulSoup
import requests
import time
import json

#from <FILE THAT INTERACTS WITH THE WEBPAGE> import playlist_url

time.sleep(1) ##For safety
##Will need to learn how to get the url from the chrome interphase. Problem for a later day
playlist_url = 'https://8tracks.com/nothyme1/please-study-you-re-failing' ##Random page I pulled for testing
response = requests.get(playlist_url)
soup = BeautifulSoup(response.text, 'html.parser')

##Need to store: The Song, The Artist -> For the actual spotify playlist
    ##Also need: The cover image, the notes, the maker of the playlist

disc = soup.find("meta", {'property':'og:description'})['content'].replace('\n','') ##Strip out breaks for use in spotify disc
author = str(soup.find("meta", {'property':'music:creator'})['content']).split('/')[-1]
title = soup.find("meta", {'property':'og:title'})['content']
cover = soup.find("meta", {'property':'og:image'})['content']

##Store this info in a json
data = {
    'Description': disc + " A playlist by " + author + ". Made using <Name of what I'm calling this>",
    'Title': title,
    'Cover': cover
}
with open("./store/meta.json", 'w') as outfile:
    json.dump(data, outfile)

