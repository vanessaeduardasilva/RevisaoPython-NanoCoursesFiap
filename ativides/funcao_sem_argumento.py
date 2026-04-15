def calcular_velocidade_media():
    #codigo da nossa função
    velocidade_media = distancia / tempo
    #exibir resultado
    print(f"A média é {velocidade_media}")

#solicitar distância e tempo
distancia = float(input("Digite a distância percorrida: "))
tempo  = float(input("Digite o tempo da viagem: "))
calcular_velocidade_media()

#função sim argumento so devem ser utilizadas quando não se tem valores previos