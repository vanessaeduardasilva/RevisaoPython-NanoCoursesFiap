opcao = 0

while opcao != 3:
    print("1 - Receber um elogio")
    print("2 - Calcular o fatorial")
    print("3 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Você é uma pessoa muito inteligente!")

    elif opcao == 2:
        # calculo do fatorial
        numero = int(input("Por favor informe o numero do qual deseja o fatorial: "))
        fat = numero

        for valor in range(1, numero, 1):
            fat = fat * valor

        print(f"O fatorial para o valor informado é: {fat}")

    elif opcao == 3:
        print("Saindo do sistema!")
            
    else:
        print("Escolha uma opção do menu!")    