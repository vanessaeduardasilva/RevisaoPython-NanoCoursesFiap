#kwargs argumentos que são relacionados a palavra chave
def exibe_ficha(**dados): #"**" o py entende que pode passar dento dos parenteses ao chamar a função colocar argumentos.
    print("---FICHA---")
    for chave, valor in dados.items():
        print(f"{chave.upper()} - {valor}")

exibe_ficha(nome="Dino da Silva", estado_civil="Casado")

ficha_cliente = {
    "nome": "Dino da Silva Bezerra",
    "estado civil": "casado",
    "camisa": "Azul Marinho",
    "Filhos": True

}

exibe_ficha(**ficha_cliente)