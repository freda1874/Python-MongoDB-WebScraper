import requests
from bs4 import BeautifulSoup
import pymongo
import datetime

url = "https://www.weather.gc.ca/canada_e.html"
weater_Ontario = []
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.CST8276.weather_Ontario


def scrape_weather():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    table = soup.find(
        "table", class_="table table-hover table-striped table-condensed")
    headers = table.find_all("th")

    titles = []
    for i in headers:
        title = i.text
        titles.append(title)

    rows = table.find_all("tr")

    for i in rows[1:]:
        data = i.find_all("td")
        row = [tr.text.strip() for tr in data]
        weater_Ontario_city = {}
        for num in range(3):
            weater_Ontario_city[titles[num]] = row[num]
        weater_Ontario_city["last_modified"] = datetime.datetime.now(
            tz=datetime.timezone.utc)
        weater_Ontario.append(weater_Ontario_city)
    return weater_Ontario


weather = scrape_weather()
try:
    db.insert_many(weater_Ontario)
    print(f'inserted {len(weater_Ontario)} items')
except:
    print('an error occurred quotes were not stored to db')
