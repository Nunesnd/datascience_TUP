"""
Matrizes, usamos indices para encontrarmos as informações
"""

pessoas = []

while True:
    print("-"*30)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar usuário')
    print('2 - Listar usuários')
    print('3 - Sair')
    
    opcao = input()
    
    if opcao == "1":
        nome = input('Digite o nome: ')
        idade = input('Digite o idade: ')
        cidade = input('Digite o cidade: ')
        
        pessoas.append([nome, idade, cidade])
        
    elif opcao == "2":
        
        for pessoa in pessoas:
            
            print("-"*30)
            print(f'Nome: {pessoa[0]}')
            print(f'Idade: {pessoa[1]}')
            print(f'Cidade: {pessoa[2]}')
            
    elif opcao == "3":
        break