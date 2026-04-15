def soma(a,b): # essa função retorna dados para quem a chamou
    resultado = a + b
    return resultado

valor1 = int(input("Informe o primeiro valor que deseja somar "))
valor2 = int(input("Informe o segundo valor que deseja somar "))

resposta = soma(valor1, valor2)
print(f"A resposta é {resposta}")