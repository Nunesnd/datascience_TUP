import os
from time import sleep
    
def cadastrar(pessoas):
    pessoa = {}
    pessoa["nome"] = input('Digite o nome: ')
    pessoa["idade"] = input('Digite a idade: ')
    pessoa["cidade"] = input('Digite a cidade: ')
    
    pessoas.append(pessoa) # usando lista de dict
    
    print('\nCadastro realizado com sucesso!\n')
    
    return pessoas
    
    sleep(1)  # Aguarda 2 segundos antes de continuar


def listar(pessoas):
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
    return f"Nome: {pessoa['nome']}\nIdade: {pessoa['idade']}\nCidade: {pessoa['cidade']}"
