import json

import requests


def get_data(label: str) -> dict:
    url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"

    print(f"Procurando por vagas '{label}'...")

    r = requests.get(url)
    response = r.json()
   
    return response
