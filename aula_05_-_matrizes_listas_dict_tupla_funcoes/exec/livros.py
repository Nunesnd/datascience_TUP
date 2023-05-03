import cadastra.cad_livros as fn_livros
import navega.menus as fn_telas

livros = []

while True:
    fn_telas.menu_prin()
    
    opcao = input()
    
    if opcao == '1':
        livros = fn_livros.cadastrar(livros)
    
    elif opcao == '2': 
        livros = fn_livros.listar(livros)
    
    elif opcao == "3":        
        fn_telas.sair("Encerrando o programa...")
        break
    
    else:
        fn_telas.sair('Opção inválida, tente novamente')