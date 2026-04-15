#importação do OrderedDict
from collections import OrderedDict

#criação

dicionario_ordenado = OrderedDict()

#adicionando chaves e valores
dicionario_ordenado["Nome"] = "Iphone"
dicionario_ordenado["Marca"] = "Apple"
dicionario_ordenado["Modelo"] = "14 Pro Max"


#percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")

#alternando um novo item
dicionario_ordenado["Marca"] = "Maçã"
print()

#percorrendo para verificar a ordem 
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")

#removendo um item 
dicionario_ordenado.pop("Marca")
print()

#percorrendo para verificar a ordem 
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")

#reinserindo um item no dicionario
dicionario_ordenado["Marca"] = "Apple"
print()

#percorrendo para verificar a ordem 
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")