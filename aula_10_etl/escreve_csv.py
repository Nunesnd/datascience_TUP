import csv
import random

# Criação da lista de cidades e estados
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador", "Fortaleza", "Recife", "Porto Alegre", "Curitiba", "Goiânia", "Manaus", "Belém", "Vitória", "Florianópolis", "João Pessoa", "Campo Grande", "Cuiabá", "Natal", "Teresina", "São Luís"]
estados = ["SP", "RJ", "MG", "DF", "BA", "CE", "PE", "RS", "PR", "GO", "AM", "PA", "ES", "SC", "PB", "MS", "MT", "RN", "PI", "MA"]

# Criação do arquivo CSV
with open('vitimas_covid_brasil_2020.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Cabeçalho do arquivo CSV
    writer.writerow(['id', 'cidade', 'estado', 'num_vitimas'])
    
    # Geração de 150 linhas aleatórias
    for i in range(1, 2001):
        cidade = random.choice(cidades)
        estado = estados[cidades.index(cidade)]
        num_vitimas = random.randint(1, 100)
        
        # Escrita da linha no arquivo CSV
        writer.writerow([i, cidade, estado, num_vitimas])
