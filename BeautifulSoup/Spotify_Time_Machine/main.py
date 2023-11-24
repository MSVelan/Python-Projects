from bs4 import BeautifulSoup
import requests
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

import os
from dotenv import load_dotenv
import base64

load_dotenv()

dirName = os.path.dirname(__file__)
fileName = os.path.join(dirName,"cover_img.jpeg")

hitsEndpoint = "https://www.billboard.com/charts/hot-100/"

date = input("Enter the date to find top songs at that time (YYYY-MM-DD) format: ")

# date = "2023-04-22"

response = requests.get(url=f"{hitsEndpoint}{date}/")
songsWebsite = response.text

soup = BeautifulSoup(songsWebsite, "html.parser")
songs = soup.find_all(name="ul", class_="o-chart-results-list-row")
songTitles = [a.h3.getText() for a in songs]
songBy = [a.ul.span.getText() for a in songs]
# print(songBy)

def removeNewline(s):
    return ''.join(s.split("\n"))

def removeTabs(s):
    return ''.join(s.split("\t"))

for i in range(len(songTitles)):
    songTitles[i] = removeTabs(removeNewline(songTitles[i]))
    songBy[i] = removeTabs(removeNewline(songBy[i]))

# print(len(songTitles))
# print(songTitles)

clientId = os.environ["SPOTIPY_CLIENT_ID"]
clientSecret = os.environ['SPOTIPY_CLIENT_SECRET']
redirectURL = os.environ['SPOTIPY_REDIRECT_URI']

scope = "playlist-modify-public"

token = util.prompt_for_user_token('USERNAME_TO_AUTHORIZE',scope,client_id=clientId,client_secret=clientSecret,redirect_uri=redirectURL)

sp = spotipy.Spotify(auth=token)

username = sp.current_user()['id']

playlistId = sp.user_playlist_create(user=username,name=f"Top 100 songs in {date}",public=True,description=f"This playlist contains the top 100 songs on {date} taken from Billboard website")

with open(fileName, "rb") as f:
    convertedString = base64.b64encode(f.read())

playlistId = playlistId['id']

# sp.playlist_upload_cover_image(playlist_id=playlistId, image_b64=convertedString)

header = {
    "Authorization": token,
    "Content-Type": "image/jpeg"
}
response = requests.put(url=f"https://api.spotify.com/v1/playlists/{playlistId}/images",params=convertedString)
print(response.text)
print()
urls = []

for i in range(len(songTitles)):
    song = songTitles[i]
    # print(song, " ", songBy[i])
    query = f"track: {song} {songBy[i]} year: {date.split('-')[0]}"
    result = sp.search(q=query,limit=1, offset=0, type="track", market=None)
    if(result!=None):
        print(result['tracks']['items'][0]['external_urls']['spotify'])
        urls.append(result['tracks']['items'][0]['external_urls']['spotify'])


sp.playlist_add_items(playlist_id=playlistId, items=urls)
print("Done")
# pprint(urls)