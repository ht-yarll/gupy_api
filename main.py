import os
import json

from utils.get_url import get_url

label = 'dados'
data = get_url(f'{label}')

os.makedirs('vagas/', exist_ok=True)

file_path = os.path.join('vagas', f'{label}.json')


with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)




