import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
load_dotenv()
import json

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv("client_id"),client_secret=os.getenv("client_secret")))

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

artist = sp.artist(urn)
# print(artist)

user = sp.user('plamere')
# print(user)

# q* track:nightcrawler artist:travis scott
#q = album:arrival artist:abba
# type* track
q = "track:nightcrawler artist:travis scott"
output = sp.search(q, limit=1, offset=0, type='track', market=None)
# print(output)
print(output["tracks"]["items"][0]["album"]["artists"])
print(output["tracks"]["items"][0]["album"]["artists"])