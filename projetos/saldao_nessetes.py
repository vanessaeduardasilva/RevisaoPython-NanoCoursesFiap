#Uma loja muito renomada da grande empresaria Vanessa Cunha oferece pagamentos por boleto bancario ou por cartão de credito. 
#Osclientes que pagam atraves de boleto têm direito à 5% de desconto sobre o valor da compra, enquanto os clientes que pagam
#em cartão de crédito podem escolher parcelar em até 12x.

#IF COMPOSTO

print("Saldão da Nessete!")

total_compra = float(input("Por favor, informe o valor total da compra do cliente: "))
forma_pagamento = int(input("Selecione a forma de pagamento: \n\t1-BOLETO\n\t2-CARTÃO "))

if forma_pagamento == 1:
    #descontex
    total_compra_desconto = total_compra * 0.95
    print(
        f"O total da compra de R${total_compra:.2f} sofreu um desconto pelo pagamento em boleto."
        f"\nO cliente deverá pagar R${total_compra_desconto:.2f}."
    )

else:
    #parcelento
    
        parcelas = int(input("Por favor, informe a quantidade de parcelas: "))
        valor_parcela = total_compra / parcelas
        print(
              f"O total da compra de R${total_compra:.2f} sera pago em {parcelas} de R$ {valor_parcela:.2f}."
              )
    
