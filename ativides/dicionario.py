#dados
#Stars Wars - Ep. IV - uma nova esperança, George Lucas, 1977, 775000000.00
#criação do dicionario
dicionario = {
    "nome": "Stars Wars - Ep. IV - uma nova esperança",
    "diretor": "George Lucas",
    "ano de lançamento": 1977,
    "bilheteiria": 775000000.00
}

#exibir dicionario completo
print(dicionario)

#exibir um valor de uma chave especifica 
print(dicionario["nome"])

#inserir novo valor no dicionario
dicionario["gênero"] = "Space Opera"

#metodo keys
print(dicionario.keys())

for chave in dicionario.keys():
    print(chave)

#metodo values
print(dicionario.values())
for valor in dicionario.values():
    print(valor)

#método items()
print(dicionario.items())    
for chave, valor in dicionario.items():
    print (f"{chave}  --- {valor}")

#metodo get
print(dicionario.get("publico"))

#metodo  setdefault
dicionario.setdefault("publico", 1000)
print(dicionario)
dicionario.setdefault("publico", 9000)
print(dicionario)
