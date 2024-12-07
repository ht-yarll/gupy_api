import os
import json

from utils.get_url import get_data

import pandas as pd
import matplotlib.pyplot as plt

label = 'dados'


df_normalize = pd.json_normalize(get_data(label))



df = pd.DataFrame(df_normalize)


print(df)


