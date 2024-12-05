import os
import json

from utils.get_url import get_url

data = get_url('dados')

d = []
for i in data:
    values = {
        'id': i['id'],
        'nome': i['name'],
        'cidade': i['city'],
        'modelo': i['workplaceType'],
        'url da vaga': i['jobUrl'],
    }

    d.append(values)

print(d)

# os.makedirs(f'vagas/{label}.json')



