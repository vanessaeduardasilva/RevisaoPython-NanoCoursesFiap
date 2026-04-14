#projeto para consolidar os conhecimentos

#NOME
#PESO
#ALTURA
#IDADE
#TEM PESO MINIMO PARA DOAR
#TEM IDADE MINIMA PARA DOAR

print("Cadastro de doadores de sangue")
nome = input("Por favor, informe o seu nome completo: ")
peso = float(input("Por favor, informe o seu peso em Kg: "))
altura = int(input("Por favor, informe a sua altura em cm: "))
ano_nascimento = int(input("Por favor, informe o seu ano de nascimento: "))

idade = 2026 - ano_nascimento
tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 16

texto_saida = (
    f"\tNOME: {nome}\n"
    f"\tPESO: {peso} kg\n"
    f"\tALTURA: {altura} cm\n"
    f"\tIDADE: {idade}\n"
    f"\tITEM PESO MINIMO PARA DOAR: {tem_peso_minimo}\n"
    f"\tITEM IDADE MINIMA PARA DOAR: {tem_idade_minima}"
)

print(texto_saida)