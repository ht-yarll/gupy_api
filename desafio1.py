import os
import json

from utils.get_url import get_data


try:
    label = 'cuidador'
    data = get_data(f'{label}')

    os.makedirs('vagas/', exist_ok=True)

    file_path = os.path.join('vagas', f'{label}.json')

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

except Exception as e:
   print(f'I have a bad feeling about this: {e}')




