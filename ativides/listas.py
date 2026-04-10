lista = [12, 15.5, "textos"]

print(type("lista"))

#inserindo novos elementos
#"lista.insert("teste de inserção")", coloca novos valores na lista, o nome da lista é "lista"
lista.append("Teste de inserção")

#mostrando a lista inteiro
print(lista)

#mostrando elemento pelo indice, cada elemento tem um numero "indice" para ele, 
#na minha lista o 12 seria o zero, e o 15.5 o um e por ai vai.
print(lista[0]) #exibe o elemento twenty girlll. 

#exibir ultimo valor da lista
#"print(lista[-1]) - Ultimo elemento da lista", #"print(lista[-2]) - penultimo elemento da lista" e por ai vai..

#exibir por intervalos
#"print(lista[0;3])"

#exibindo com loop
for valor in lista:
    print(valor)

#removendo
lista.pop()
print(lista)

#ou para remover um elemento especifico
lista.remove(12)
print(lista)

#tamanho da lista
print(len(lista))

