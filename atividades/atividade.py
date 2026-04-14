#Criando um mini projetinho para praticar os conceitos de entrada de dados, variáveis e operações matemáticas.

print("Bem Vindo a CALCULADORA DE MÉDIA DE NOTAS!")

nome = (input("Por favor, digite o nome do Aluno: "))
nota1 = float(input("Digite a primeira nota: "))   
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media_nota = ((nota1 + nota2 + nota3 + nota4)/4)

print(f"O aluno {nome} teve a média de notas: {media_nota:.2f}")