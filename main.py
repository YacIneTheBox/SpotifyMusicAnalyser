import csv
import json

import requests

with open(
    "Ressources/spotify-tracks-dataset.csv", "r", newline="", encoding="utf-8"
) as file:
    reader = csv.reader(file, delimiter=",")
    # for row in reader:
    # print(row)

API_KEY = "5dcf90c78b7557abbf9f50cf71943afa"
USER_AGENT = "Groovy1.0"


def get_top_artist_by_tag(tag):
    url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists&tag={tag}&api_key={API_KEY}&format=json"
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        artists = data["topartists"]["artist"]
        names = [a["name"] for a in artists]
        return names
    else:
        print(f"Error: {response.status_code}")


data_brut = get_top_artist_by_tag("jazz")

print(data_brut)
