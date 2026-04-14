#criando um set vazio

conjunto = set()
print(type(conjunto))

#criando um set a partir de uma lista
lista = ["Vanessa", "Cunha", "Magali","Vanessa"]
print(lista)
conjunto2 = set(lista)
print(conjunto2)

#criando um set com valores
conjunto3 = {"Cebolinha", "Magali", "Monica", "Cascão", "Cebolinha"}
print(conjunto3)

#adicionando um elemento (add)
conjunto3.add("Franjinha")
print(conjunto3)

#removendo elementos que estão em outro set (difference_update)

conjunto1 = {"Mega Drive", "Super Nitendo", "Playstation"}
conjunto4 = {"Playstation", "Nitendo 64", "Sega Saturn", "Dreamcast"}

print(f"O primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto4}")

conjunto1.difference_update(conjunto4)

print(f"O primeiro set agora contém {conjunto1}")

#remover um elemento específico do set (remove) - quando usa o remove e o valor não esta no set, gera um erro
conjunto1 = {"Mega Drive", "Super Nitendo", "Playstation"}
print(conjunto1)
conjunto1.remove("Mega Drive")
print(conjunto1)

#remover um elemento específico do set (discard) - quando usa o discard e o valor não esta no set, ele apaga, e não gera um erro
conjunto1.remove("Super Nintendo")
print(conjunto1)
conjunto1.discard("Super Nintendo")
print(conjunto1) 