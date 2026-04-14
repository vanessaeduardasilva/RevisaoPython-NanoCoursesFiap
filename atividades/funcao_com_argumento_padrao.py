def calcular_velocidade_media(distancia:float, tempo:float, unidade_medida ="Km\h"): #criando argumentos, serve para garantir que seja insrerido um nunmero
    #codigo da nossa função
    velocidade_media = distancia / tempo
    #exibir resultado
    print(f"A velocidade média é {velocidade_media}{unidade_medida}")


calcular_velocidade_media(200, 3,)

calcular_velocidade_media()

