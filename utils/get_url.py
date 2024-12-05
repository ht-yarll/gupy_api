import json

import requests


def get_url(label: str):
    url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"

    print(f"Procurando por vagas '{label}'...")

    r = requests.get(url)
    
    return r.json()
    

    