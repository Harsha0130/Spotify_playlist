import spotipy
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ["SPOTIFY_ID"]
client_secret = os.environ["SPOTIFY_SECRET"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="314ygud37bcy2eerf4oszqodrobi",
    )
)
user_id = sp.current_user()["id"]

#
# date = input("Which year do you want to travel to? "
#              "Type the date in this format YYYY-MM-DD: ")
#
# date_ = datetime.strptime(date, "%d-%m-%Y")
# formatted_date = date_.strftime("%Y-%m-%d")
# print(formatted_date)
#
# URL = f"https://www.billboard.com/charts/hot-100/{formatted_date}/"
#
# response = requests.get(url=URL)
# data = response.text
#
# soup = BeautifulSoup(data, "html.parser")
#
# song_title = soup.select("li ul li h3")
#
#
# song_list = [song.getText().strip() for song in song_title]
# print(song_list)
#




