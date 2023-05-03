import csv

# Abre o arquivo CSV
with open('vitimas_covid_brasil_2020.csv', mode='r', encoding='utf-8') as file:
    # Cria um objeto leitor CSV
    reader = csv.reader(file)
    
    # Lê o cabeçalho
    header = next(reader)
    
    # Imprime o cabeçalho
    print(header)
    
    # Imprime as linhas do arquivo
    for row in reader:
        print(row)
