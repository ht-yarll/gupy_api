import os
import json
import re
import openpyxl

from utils.get_url import get_data
from utils.chartmaker import df_vagas_por_estado
from utils.chartmaker import df_vagas

import pandas as pd
import matplotlib.pyplot as plt


# Correlação de Numero de Vagas por Estado
fig_path = os.path.join('vagas', 'vagas_por_estado.png')

fig, ax = plt.subplots(figsize=(16, 6))


ax.barh(df_vagas_por_estado['state'], df_vagas_por_estado['vagas_por_estado'], color='#238c83')
ax.set_facecolor('#161717')

fig.suptitle('Quantidade de Vagas')

plt.grid(color='grey', linestyle='--', linewidth = 0.5)
plt.figtext(0.65, 0.89, 'Gupy Api', fontsize=8)

plt.yticks(fontsize=10)
plt.xticks(fontsize=8)

plt.xlabel('Nº de Vagas')

plt.ylabel('Vagas')


plt.savefig(fig_path)


#saving file
file_path = os.path.join('vagas', 'vagas_table.xlsx')

df_vagas.to_excel(file_path, index=False)