import json

with open("arquivo.json", mode="r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.read()

conteudo_convertido = json.loads(conteudo)


print(conteudo_convertido)
print(type(conteudo_convertido))