op = 0
ficha = {}

while op !=4:
    print("\nFICHA CADASTRAL")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informações da ficha")
    print("3 - Exibir a ficha completa")
    print("4 - Sair")
    op = int(input("Informe a opção desejada: "))

    if op == 1:
        #inserir dados na ficha
        chave = input("Informe o campo que deseja cadastrar na ficha: ") 
        valor = input("Informe o dado que deseja cadastrar neste campo: ") 
        ficha.update({chave:valor})

    elif op == 2:
        #recuperar dados da ficha
        print(f"Os campos diponiveis na ficha são {ficha.keys()}")
        chave = input("Informe qual campo deseja exibir: ")
  
        if chave in ficha.keys():
            print(f"O campo {chave} contém o dado {ficha.get[chave]}")
        else: 
            print("Você digitou um campo inexistente.")  

    elif op == 3:
        #exibir a ficha completa
        print("FICHA CADASTRAL")
        for campo, dado in ficha.items():
            print(f"{campo.upper()} ---> {dado}")
    
    elif op == 4:
        print("Saindo do sistema de ficha cadastral")
        break
    else:
        print("Por favor, escolha uma opção válida")    