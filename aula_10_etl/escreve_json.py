import json
import random

# Criação da lista de cidades e estados
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador", "Fortaleza", "Recife", "Porto Alegre", "Curitiba", "Goiânia", "Manaus", "Belém", "Vitória", "Florianópolis", "João Pessoa", "Campo Grande", "Cuiabá", "Natal", "Teresina", "São Luís"]
estados = ["SP", "RJ", "MG", "DF", "BA", "CE", "PE", "RS", "PR", "GO", "AM", "PA", "ES", "SC", "PB", "MS", "MT", "RN", "PI", "MA"]

# Lista que irá armazenar as linhas
linhas = []

# Geração de 150 linhas aleatórias
for i in range(1, 151):
    cidade = random.choice(cidades)
    estado = estados[cidades.index(cidade)]
    num_vitimas = random.randint(1, 100)

    # Adiciona a linha na lista
    linhas.append({
        'id': i,
        'cidade': cidade,
        'estado': estado,
        'num_vitimas': num_vitimas
    })

# Criação do arquivo JSON
with open('vitimas_covid_brasil_2020.json', mode='w', encoding='utf-8') as file:
    json.dump(linhas, file, ensure_ascii=False, indent=4)
