import csv

# Abre o arquivo CSV
with open('vitimas_covid_brasil_2020.csv', mode='r', encoding='utf-8') as file:
    # Cria um objeto leitor CSV
    reader = csv.reader(file)
    
    # Pula o cabeçalho
    next(reader)
    
    # Cria um dicionário para acumular o número de vítimas por estado
    vitimas_por_estado = {}
    
    # Acumula o número de vítimas por estado
    for row in reader:
        estado = row[2]
        num_vitimas = int(row[3])
        if estado in vitimas_por_estado:
            vitimas_por_estado[estado] += num_vitimas
        else:
            vitimas_por_estado[estado] = num_vitimas
    
    # Ordena os resultados por número de vítimas
    resultados_ordenados = sorted(vitimas_por_estado.items(), key=lambda x: x[1], reverse=True)
    
    # Imprime os resultados
    for estado, num_vitimas in resultados_ordenados:
        print(f"{estado}: {num_vitimas} vítimas")
