import csv
import funcao

import os

os.environ['PYTHONIOENCODING'] = 'utf-8'
# passo a passo de um processo ETL

# ===== inicio "Extract" =======
lista_vitimas_covid = []
with open('vitimas_covid_brasil_2020.csv', mode='r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)  # pula a primeira linha (cabeçalho)
    for row in csv_reader:
        lista_vitimas_covid.append({
            "id": row[0],
            "cidade": row[1],
            "estado": row[2],
            "vitimas": int(row[3]),
        })
        
# ===== fim "Extract" =======

# ===== inicio "Transform" =======
lista_vitimas_sumarizada = {}
for vitima in lista_vitimas_covid:
    estado = vitima["estado"]

    vitimas_somadas = 0
    if not estado in lista_vitimas_sumarizada:
        lista_vitimas_sumarizada[estado] = {"vitimas": 0}
    else:
        vitimas_somadas = int(lista_vitimas_sumarizada[estado]["vitimas"])

    lista_vitimas_sumarizada[estado] = {
        "cidade": vitima["cidade"],
        "estado": vitima["estado"],
        "vitimas": int(vitima["vitimas"]) + vitimas_somadas
    }
    
# # ===== fim "Transform" =======

# print(len(lista_vitimas_sumarizada))
# for estado in lista_vitimas_sumarizada:
#     print(lista_vitimas_sumarizada[estado])

# # ===== inicio "Load" =======

for estado in lista_vitimas_sumarizada:
    cidade = lista_vitimas_sumarizada[estado]["cidade"]
    estado = lista_vitimas_sumarizada[estado]["estado"]
    vitimas = lista_vitimas_sumarizada[estado]["vitimas"]
    funcao.inserir_postgre(cidade, estado, vitimas)

# # ===== fim "Load" =======

print('Processo de ETL executado com sucesso!')