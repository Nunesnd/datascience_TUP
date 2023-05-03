"""
Dict, usamos chaves para encontrarmos as informações
"""

import funcoes_tela as fnt
import funcoes_pessoas as fnp



while True:
    fnt.menu()
    
    opcao = input()
    
    if opcao == "1":
        fnp.cadastrar()
        
    elif opcao == "2":
        fnp.listar()
         
    elif opcao == "3":        
        fnt.sair("Encerrando o programa...")
        break
    
    else:
        fnt.sair('Opção inválida, tente novamente')
       
