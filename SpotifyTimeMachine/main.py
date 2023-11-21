import os

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")

###Scraping Billboard 100
URL = ("https://www.billboard.com/charts/hot-100/" + date)
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
#print(song_names)

###SPOTIFY AUTH

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=os.environ['username']
    )
)

user_id = sp.current_user()["id"]
#print(user_id)
###SPOTIFY AUTH

###SPOTIFY SEARCH
song_uris = []
year = date.split("-")[0]
month = date.split("-")[1]
day = date.split("-")[2]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
###SPOTIFY SEARCH

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{day}-{month}-{year} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
