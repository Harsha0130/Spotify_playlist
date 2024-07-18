from datetime import datetime
import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? "
             "Type the date in this format YYYY-MM-DD:")

date_ = datetime.strptime(date, "%d-%m-%Y")
formatted_date = date_.strftime("%Y-%m-%d")

URL = f"https://www.billboard.com/charts/hot-100/{formatted_date}/"

response = requests.get(url=URL)
data = response.text




