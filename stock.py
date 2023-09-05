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

# Imprime el resultado
with open(nombre_archivo, 'r') as archivo:
    contenido_json = archivo.read()
    print(contenido_json)
    
print(f'El JSON se ha guardado en {nombre_archivo}')
