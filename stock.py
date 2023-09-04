import pandas as pd
import json

SHEET_ID = '1r8KnwTRDr5DlocXelGBzHcGcu_76dICN'
SHEET_NAME = 'STOCKWEB'
nombre_archivo = 'data.json'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

df = pd.read_csv(url)
data_dict = df.to_dict(orient='records')

with open(nombre_archivo, 'w') as archivo:
    json.dump(data_dict, archivo, indent=4)
print(f'El JSON se ha guardado en {nombre_archivo}')