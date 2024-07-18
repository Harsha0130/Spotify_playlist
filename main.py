from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup


client_id = os.environ["SPOTIFY_ID"]
client_secret = os.environ["SPOTIFY_SECRET"]

date = input("Which year do you want to travel to? "
             "Type the date in this format YYYY-MM-DD:")

date_ = datetime.strptime(date, "%d-%m-%Y")
formatted_date = date_.strftime("%Y-%m-%d")
print(formatted_date)

URL = f"https://www.billboard.com/charts/hot-100/{formatted_date}/"

response = requests.get(url=URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")

song_title = soup.select("li ul li h3")


song_list = [song.getText().strip() for song in song_title]
print(song_list)





