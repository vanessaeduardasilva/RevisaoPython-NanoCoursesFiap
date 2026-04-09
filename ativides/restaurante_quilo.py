print("Quilão da Vanessinha")

preco_quilo = float(input("Informe o valor cobrado por quilo: "))
peso_prato = float(input("Informe o peso do prato do cliente (em kg) "))

preco_prato = preco_quilo * peso_prato

print(f"O valor do prato é R$ {preco_prato:.2f}")

if peso_prato > 1: #IF simples
    print("Como o peso do prato do cliente ultrapassou 1kg, ele deve pagar apenas o valor fixo de R$80,00")

    
