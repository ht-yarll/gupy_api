import os
import json

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

df_vagas_list = [df_vagas_dados, df_vagas_designer, df_vagas_ux]
df_vagas = pd.concat(df_vagas_list)