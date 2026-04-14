#importação
from collections import defaultdict

#criação de um default dict com uma lista como valor padrão
dicionario_lista = defaultdict(list)
dicionario_lista["Produto"] = "MacBook Pro"
dicionario_lista["Marca"] = "Apple"

print(dicionario_lista)

#criaçâo de funçao que retorna a frase "INEXISTENTE"
def funcao_exemplo():
    return "INEXISTENTE"
dicionario_funcao = defaultdict(funcao_exemplo)
dicionario_funcao["Produto"] = "MacBook Pro"
dicionario_funcao["Marca"] = "Apple"

print(dicionario_funcao)
print(dicionario_funcao["Preço"])


#Criação de dicionario com uma função lambda
dicionario_lambda = defaultdict(lambda:"Não disponivel")
dicionario_lambda["Produto"] = "MacBook Pro"
dicionario_lambda["Marca"] = "Apple"

print(dicionario_lambda)
print(dicionario_lambda["Preço"])
print(dicionario_lambda)




