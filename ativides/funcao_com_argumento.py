def calcular_velocidade_media(distancia, tempo): #criando argumentos, serve para garantir que seja insrerido um nunmero
    #codigo da nossa função
    velocidade_media = distancia / tempo
    #exibir resultado
    print(f"A média é {velocidade_media}")

#solicitar distância e tempo
dist_digitada = float(input("Digite a distância percorrida: "))
tempo_digitado = float(input("Digite o tempo da viagem: "))
calcular_velocidade_media(dist_digitada, tempo_digitado)

#função com argumento so devem ser utilizadas quando se tem valores previos