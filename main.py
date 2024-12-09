import os
import json
import re

from utils.get_url import get_data
from utils.chartmaker import df_vagas_consolidado

import pandas as pd
import matplotlib.pyplot as plt


# Correlação de Vagas por Estado
fig, ax = plt.subplots(figsize=(16, 6))
ax.barh(
    df_vagas_consolidado['state'], 
    df_vagas_consolidado['N_Vagas'], 
    color='#238c83'
)

ax.set_facecolor('#161717')

fig.suptitle('Relação de Quantidade de Vagas por Estado')

plt.grid(color='grey', linestyle='--', linewidth = 0.5)
plt.figtext(0.65, 0.89, 'Fonte: Gupy Api', fontsize=8)

plt.xlabel('Nº de Vagas')
plt.ylabel('Estados')

plt.show()