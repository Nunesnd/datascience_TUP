import os
from time import sleep

if os.name == 'posix':  # Unix-like (Linux, macOS)
    clear_command = 'clear'
elif os.name == 'nt':  # Windows
    clear_command = 'cls'
else:
    clear_command = None

def menu_prin():
    os.system(clear_command)  # Limpa a tela do terminal (compatível com sistemas Unix-like)
    print("-"*30)
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar livro')
    print('2 - Mostrar livros')
    print('3 - Sair')
    
def sair(msg):
    os.system(clear_command)
    print(msg)
    sleep(1)