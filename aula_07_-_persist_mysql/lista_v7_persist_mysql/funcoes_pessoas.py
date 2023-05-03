import os
from time import sleep

import models.pessoa as mod_pessoas

#import repositorios.persist_mysql as repo
#repoInstancia = repo.PersistMySQL("localhost", "root", "a1!b2@c3#ABC", "desafio21dias", "pessoas")

import repositorios.persist_postgresql as repo
repoInstancia = repo.PersistPostgreSQL("localhost", 5432, "desafio_21_dias", "postgres", "D1360nun#$", "pessoas")

#import repositorios.persist_sqlserver as repo
#repoInstancia = repo.PersistSqlServer("DESKTOP-SBORRH9", "desafio_21_dias", "sa", "a1!b2@c3#", "pessoas")
#DESKTOP-SBORRH9

#import repositorios.persist_csv as repo
#repoInstancia = repo.PersistCSV("pessoas.csv")

#import repositorios.persist_json as repo
#repoInstancia = repo.PersistCSV("pessoas.json")
    
def cadastrar():
    os.system('cls')
    print('Cadastro de pessoas\n')
    pessoa = mod_pessoas.Pessoa()
    pessoa.nome = input('Digite o nome: ')
    pessoa.idade = input('Digite a idade: ')
    pessoa.cidade = input('Digite a cidade: ')
    
    repoInstancia.incluir_pessoa(pessoa)    
        
    print('\nCadastro realizado com sucesso!\n')
    
    sleep(2)  # Aguarda 2 segundos antes de continuar
    
def listar():
    pessoas = repoInstancia.listar_pessoas()
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
    return f"Id: {pessoa.id}\nNome: {pessoa.nome}\nIdade: {pessoa.idade}\nCidade: {pessoa.cidade}"
