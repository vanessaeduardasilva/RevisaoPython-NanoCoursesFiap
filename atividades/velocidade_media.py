print("Simulador de computador de bordo!")
distancia = float(input("Por favor, informe a distância percorrida : "))
tempo = float(input("Por favor, informe o tempo da viagem em horas: "))

velocidade_media = distancia / tempo

print(f"A velocidade média da viagem foi de: {velocidade_media:.2f} km/h")
#o :.2f é para limitar a quantidade de casas decimais a 2, e o f é para formatar a string.10


print("Obrigado por usar o Simulador de computador de bordo!")