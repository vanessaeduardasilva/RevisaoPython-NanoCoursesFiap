def exibe_promocao(*clientes):  # "*" indica quantidade variável de argumentos
    for cliente in clientes:
        print(f"Olá, {cliente}! \nQueremos te avisar que a nova calça da renner está em promoção!")

lista_clientes = ["Virginia", "Maria Flor", "Vini Jr."]
exibe_promocao(*lista_clientes)
#exibe_promocao("Ana Castela")
#exibe_promocao("Paola")