"""
Dict, usamos chaves para encontrarmos as informações
"""

import os
from time import sleep

pessoas = []

while True:
    os.system('clear')  # Limpa a tela do terminal (compatível com sistemas Unix-like)
    print("-"*30)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar usuário')
    print('2 - Listar usuários')
    print('3 - Sair')
    
    opcao = input()
    
    if opcao == "1":
        pessoa = {}
        pessoa["nome"] = input('Digite o nome: ')
        pessoa["idade"] = input('Digite a idade: ')
        pessoa["cidade"] = input('Digite a cidade: ')
        
        pessoas.append(pessoa) # usando lista de dict
        
        print('\nCadastro realizado com sucesso!\n')
        sleep(2)  # Aguarda 2 segundos antes de continuar
        
    elif opcao == "2":
        os.system('clear')
        if not pessoas:
            print('Nenhum usuário cadastrado.\n')
            sleep(2)
        else:
            print("-"*30)
            print('Lista de usuários cadastrados:')
            for pessoa in pessoas:
                print("-"*30)
                print(f'Nome: {pessoa["nome"]}')
                print(f'Idade: {pessoa["idade"]}')
                print(f'Cidade: {pessoa["cidade"]}')
            
            input('\nPressione Enter para voltar ao menu principal...')
            
    elif opcao == "3":
        os.system('clear')
        print('Encerrando o programa...')
        sleep(2)
        break
