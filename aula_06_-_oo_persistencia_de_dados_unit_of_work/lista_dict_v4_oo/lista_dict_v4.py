"""
Dict, usamos chaves para encontrarmos as informações
"""
import funcoes_tela as fnt
import funcoes_pessoas as fnp

pessoas = []

while True:
    fnt.menu()
    
    opcao = input()
    
    if opcao == "1":
        pessoas = fnp.cadastrar(pessoas)
        
    elif opcao == "2":
        pessoas = fnp.listar(pessoas)
         
    elif opcao == "3":        
        fnt.sair("Encerrando o programa...")
        break
    
    else:
        fnt.sair('Opção inválida, tente novamente')
        
