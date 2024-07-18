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

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")

song_title = soup.select("li ul li h3")


song_list = [song.getText().strip() for song in song_title]


# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    if result['tracks']['items']:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"Found: {song} -> {uri}")
    else:
        # Fallback search without the year
        result = sp.search(q=f"track:{song}", type="track")
        if result['tracks']['items']:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            print(f"Found (fallback): {song} -> {uri}")
        else:
            print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(f"Playlist created: {playlist['external_urls']['spotify']}")

# Adding tracks to the playlist in batches of 100 (Spotify's limit)
for i in range(0, len(song_uris), 100):
    batch = song_uris[i:i + 100]
    sp.playlist_add_items(playlist_id=playlist['id'], items=batch)
    print(f"Added {len(batch)} songs to the playlist.")

# Verify the songs added to the playlist
playlist_tracks = sp.playlist_tracks(playlist_id=playlist['id'])
added_songs = [track['track']['name'] for track in playlist_tracks['items']]
print(f"Songs added to the playlist: {added_songs}")