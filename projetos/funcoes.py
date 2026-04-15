#função para calcular a velocidade média
def calcular_velocidade_media(distancia:float, tempo:float, unidade_medida ="Km/h"): 
    if tempo == 0:
        return 0
    velocidade_media = distancia / tempo
    return f"{velocidade_media} {unidade_medida}"

#função para converter a temperatura
def converter_temperatura(temperatura:float, unidade_medida="celsius"):
    if unidade_medida == "celsius":
        return temperatura * 1.8 + 32
    elif unidade_medida == "fahrenheit":
        return (temperatura - 32) / 1.8
    else:
        return 0

#funcao para exibir menu
def exibir_menu():
    print("MENU")
    print("1 - Calcular a velocidade média")
    print("2 - Converter a temperatura")
    print("3 - Sair")

#funcao para chamar as outras funções
def aluno_de_fisica():
    op = 0
    while op != 3:
        exibir_menu()
        op = int(input("Informe a opção desejada: "))

        if op == 1:
            distancia_percorrida = float(input("Informe a distância: "))
            tempo_viagem = float(input("Informe o tempo da viagem: "))
            medida = str(input("Informe a unidade de medida: "))
            print(f"A velocidade média é {calcular_velocidade_media(distancia_percorrida, tempo_viagem, medida)}")

        elif op == 2:
            temperatura_informada = float(input("Informe a temperatura que deseja converter: "))    
            medida = input("A temperatura informada está em celsius ou fahrenheit: ")
            print(f"O resultado da conversão é {converter_temperatura(temperatura_informada, medida)}")
            
        elif op == 3:
            print("Saindo do sistema...")    
            break

        else:
            print("Opção inválida!")
1
aluno_de_fisica()