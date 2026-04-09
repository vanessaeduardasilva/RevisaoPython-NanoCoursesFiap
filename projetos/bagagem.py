#A companhia aérea NessaAirLines permite que seus clientes do tipo premium plus pro master despachem
#bagagens de até  32kg sem nenhum custo adicional, enquanto os clientes do tipo gold pro plus, podem levar malas de 
# até 28kg sem custo adicionais e todos os demais devem pagar por quialquer bagagem despachada. 

tipo_cliente = input("Por favor, informe o tipo do cliente: PREMIUM, GOLD ou REGULAR: ")
peso_bagagem = float(input("Informe o peso da bagagem que o cliente deseja despachar: "))

if tipo_cliente == "PREMIUM":
    #o que acontece se for PREMIUM
    if peso_bagagem <= 32:
        print(
            f"Cliente {tipo_cliente} , sua bagagem está dentro do limite permitido!"
            f"Não é necessario pagar nenhum valor para despachá-la."
        )

    else: 
        peso_excedente = peso_bagagem - 32
        print(
            f"Os clientes {tipo_cliente} têm direito a despacharem bagagens de até 32kg. A bagagem atual excede este peso em {peso_excedente}kg."
            f"Por favor, dirija-se ao balção de cobrança para realizar o pagamento referente ao peso adicional."
        )

else:
    if tipo_cliente == "GOLD":  # <-- corrigido (faltava :)
        #o que acontece se for GOLD
        if peso_bagagem <= 28:
            print(
                f"Cliente {tipo_cliente}, sua bagagem está dentro do limite permitido!"
                f"Não é necessario pagar nenhum valor para despachá-la."
            )

        else: 
            peso_excedente = peso_bagagem - 28
            print(
                f"Os clientes {tipo_cliente} têm direito a despacharem bagagens de até 32kg. A bagagem atual excede este peso em {peso_excedente}kg."
                f"Por favor, dirija-se ao balção de cobrança para realizar o pagamento referente ao peso adicional."
            )

    else: 
        print(
            f"Os clientes {tipo_cliente} não têm direito à bagagem gratuita."
            f"Por favor, dirija-se ao balção de cobrança para realizar o pagamento pela bagagem."
        )