
import pandas as pd
import geopandas as gpd
import requests

def recuperation_data(url_api):
    df = []  # Liste pour accumuler les données
    current_url = url_api

    while current_url:
        req = requests.get(current_url)
        wb = req.json()
        df.extend(wb['data'])
        current_url = wb["links"].get("next")
    return pd.DataFrame(df)

    def extraire_arrondissement(code_postal):
    try:
        arrondissement = int(code_postal[-2:])  # Récupérer les deux derniers chiffres
        return f"751{arrondissement:02d}"
    except ValueError:
        return "Arrondissement inconnu"  # Gérer les cas où le code postal est invalide