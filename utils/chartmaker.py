import os
import json
import re

from utils.get_url import get_data

import pandas as pd
import matplotlib.pyplot as plt

label = 'dados'

pd.set_option('display.max_rows', None)

label_dados = 'dados'
label_designer = 'designer'
label_ux = 'ux'


# Transformando dados em Dataframe
df_vagas_dados = pd.DataFrame((get_data(label_dados))['data']) 
df_vagas_designer = pd.DataFrame((get_data(label_designer))['data']) 
df_vagas_ux = pd.DataFrame((get_data(label_ux))['data']) 

# Creating the work Dataframe
df_vagas_list = [df_vagas_dados, df_vagas_designer, df_vagas_ux]
df_vagas = pd.concat(df_vagas_list)
df_vagas = (df_vagas
 .reset_index()
 .replace(r'^\s*$', 'Dado Não Disponível', regex=True)
 )

# Polishing
def check_category(x = str):
    if 'dados' in x.lower():
        return 'Dados'
    elif 'designer' in x.lower():
        return 'designer'
    else:
        return 'UX/UI'


df_vagas_consolidado = (
    df_vagas
    .groupby('state')
    .agg(
        vaga_para = ('name', lambda x: check_category(x.iloc[0])),
        mdt_mais_frequentes = ('workplaceType', pd.Series.mode),
        N_Vagas = ('state', 'count'),
    )
    .reset_index()
)