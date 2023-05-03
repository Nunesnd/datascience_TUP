import csv
import menu_uf
#========= inicio EXTRAC ETL

lista_vit = []
with open('vitimas_covid_brasil_2020.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    for row in reader:
        lista_vit.append({
          "id": row[0],  
          "cidade": row[1],  
          "estado": row[2],  
          "vitimas": row[3]  
        })
#========= fim EXTRAC ETL

#========= inicio TRANSFORM ETL

lst_uf = []

menu_uf.menu()

unid_fed = str(input("Escolha um estado (UF) para ter os detalhes: "))

for vitm in lista_vit:
    if vitm['estado'] == unid_fed.upper():
        lst_uf.append(vitm)    

soma = 0
#mostrar caso a caso por linha
for c in lst_uf:
    print(c)
    soma += int(c['vitimas'])




    
#========= fim TRANSFORM ETL

print(f'Totalizando no estado {soma} fatalidades em {len(lst_uf)} cidades.')