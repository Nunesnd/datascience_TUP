import os
from time import sleep

def menu():
    os.system('cls')  # Limpa a tela do terminal (compatível com sistemas Unix-like)
    print("-"*30)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar usuário')
    print('2 - Listar usuários')
    print('3 - Sair')
    
def sair(msg):
    os.system('cls')
    print(msg)
    sleep(1)