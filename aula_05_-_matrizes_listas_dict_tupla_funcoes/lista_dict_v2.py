"""
Dict, usamos chaves para encontrarmos as informações
"""

import os
from time import sleep
from turtle import clear

def menu():
    os.system('cls')  # Limpa a tela do terminal (compatível com sistemas Unix-like)
    print("-"*30)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar usuário')
    print('2 - Listar usuários')
    print('3 - Sair')
    
def cadastrar():
    pessoa = {}
    pessoa["nome"] = input('Digite o nome: ')
    pessoa["idade"] = input('Digite a idade: ')
    pessoa["cidade"] = input('Digite a cidade: ')
    
    pessoas.append(pessoa) # usando lista de dict
    
    print('\nCadastro realizado com sucesso!\n')
    sleep(1)  # Aguarda 2 segundos antes de continuar


def listar():
    os.system('cls')
    if not pessoas:
        print('Nenhum usuário cadastrado.\n')
        sleep(1)
    else:
        print("-"*30)
        print('Lista de usuários cadastrados:')
        for pessoa in pessoas:
            print("-"*30)
            print(f'')
            result = pessoa_formatada(pessoa)
            print(result)
            
        input('\nPressione Enter para voltar ao menu principal...')
           
def pessoa_formatada(pessoa):
    #return f"""
    #    Nome: {pessoa['nome']}
    #    Idade: {pessoa['idade']}
    #    Cidade: {pessoa['cidade']}
    #"""
    return f"Nome: {pessoa['nome']}\nIdade: {pessoa['idade']}\nCidade: {pessoa['cidade']}"

def sair(msg):
    os.system('cls')
    print(msg)
    sleep(1)

pessoas = []

while True:
    menu()
    
    opcao = input()
    
    if opcao == "1":
        cadastrar()
        
    elif opcao == "2":
         listar()
         
    elif opcao == "3":        
        sair("Encerrando o programa...")
        break
    
    else:
        sair('Opção inválida, tente novamente')
        
