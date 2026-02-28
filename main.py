import csv
import json

import pandas as pd
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
    headers = {"User-Agent": USER_AGENT}
    base_url = "http://ws.audioscrobbler.com/2.0/"
    parametres = {
        "method": "tag.gettopartists",
        "tag": tag,
        "api_key": API_KEY,
        "format": "json",
    }
    try:
        response = requests.get(base_url, params=parametres, headers=headers)
        response.raise_for_status()

        data = response.json()
        print("Donnée récupérée avec succès")
        artists = data["topartists"]["artist"]

        list = []

        for a in artists:
            nom_a = a["name"]
            id_unique = a["mbid"]
            rang = a["@attr"]["rank"]

            artiste_propre = {
                "Nom": nom_a,
                "MBID": id_unique,
                "Rang": int(rang),
            }
            list.append(artiste_propre)

        df = pd.DataFrame(list)
        return df

    except requests.exceptions.Timeout:
        print("Le serveur a répondu en temps écoulé")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


data_brut = get_top_artist_by_tag("rock")

print(data_brut.head())
