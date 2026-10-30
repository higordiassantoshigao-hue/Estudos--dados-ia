sistema_ativo = True

while sistema_ativo == True:
    comando = input("Digite um comando (ou 'sair' para fechar o sistema): ")
    
    if comando == "sair":
        print("Desligando o sistema de monitoramento... Até logo!")
        sistema_ativo = False 
    else:
        print("Executando o comando:", comando, "... [OK]")
