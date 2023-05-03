import os
from time import sleep

import models.pessoa as mod_pessoas
#import repositorios.persist_json as repo
import repositorios.persist_csv as repo
    
def cadastrar():
    os.system('cls')
    print('Cadastro de pessoas\n')
    pessoa = mod_pessoas.Pessoa()
    pessoa.nome = input('Digite o nome: ')
    pessoa.idade = input('Digite a idade: ')
    pessoa.cidade = input('Digite a cidade: ')
    
    #repo.PersistJson("pessoas.json").incluir_pessoa(pessoa)
    repo.PersistCSV("pessoas.csv").incluir_pessoa(pessoa)
        
    print('\nCadastro realizado com sucesso!\n')
    
    sleep(2)  # Aguarda 2 segundos antes de continuar
    
def listar():
    #pessoas = repo.PersistJson("pessoas.json").listar_pessoas()
    pessoas = repo.PersistCSV("pessoas.csv").listar_pessoas()
    os.system('cls')
    if not pessoas:
        print('Nenhum usuário cadastrado.\n')
        sleep(1)
    else:
        print("-"*30)
        print('Lista de usuários cadastrados:')
        for pessoa in pessoas:
            print("-"*30)
            result = pessoa_formatada(pessoa)
            print(result)
            #return result
        
        input('\nPressione Enter para voltar ao menu principal...')
           
def pessoa_formatada(pessoa):
    return f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}\nCidade: {pessoa.cidade}"
