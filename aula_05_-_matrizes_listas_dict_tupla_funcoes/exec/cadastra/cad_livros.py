import os
from time import sleep
    
if os.name == 'posix':  # Unix-like (Linux, macOS)
    clear_command = 'clear'
elif os.name == 'nt':  # Windows
    clear_command = 'cls'
else:
    clear_command = None
    
def cadastrar(livros):
    livro = {}
    livro["titulo"] = input('Digite o título: ')
    livro["autor"] = input('Digite a autor: ')
    livro["ano"] = input('Digite a ano: ')
    
    livros.append(livro) # usando lista de dict
    
    print('\nCadastrado com sucesso!\n')
    
    return livros
    
    sleep(1)  # Aguarda 2 segundos antes de continuar

def listar(livros):
    os.system(clear_command)
    if not livros:
        print('Nenhum título na base.\n')
        sleep(1)
    else:
        print("-"*30)
        print('Lista de usuários cadastrados:')
        for livro in livros:
            print("-"*30)
            print(f'')
            result = apresenta_livro(livro)
            print(result)
            
        input('\nPressione Enter para voltar ao menu principal...')
           
def apresenta_livro(livro):
    return f"Título: {livro['titulo']}\nAutor: {livro['autor']}\nAno: {livro['ano']}"
