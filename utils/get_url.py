import json

import requests


def get_url(label: str) -> dict:
    url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"

    print(f"Procurando por vagas '{label}'...")

    r = requests.get(url)
    if r.status_code == 200:
        try:
            data = json.loads(r.text)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}
    else:
        print(f"Failed to fetch data: {r.status_code}")
        return {}