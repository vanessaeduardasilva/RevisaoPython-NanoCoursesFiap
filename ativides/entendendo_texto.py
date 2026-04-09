texto = "Este texto quebra de linha \naqui. Porém aqui temos uma\ttabulação" #o \n é para dar uma quebra de linha, e o \t é para dar um "tab"
print(texto)

texto = "texto em minusculas AINDA É texto"
print(texto.capitalize())  #deixa a preimeira letra do texto em maiuscula.

#repare que eu coloquei o nome da varivel antes e depois o capitalize.

print(texto.upper()) #vai deixar todas as letras em maiusculo.
print(texto.lower()) #vai deixar todas as letras em minusculo.

#verificar se o meu texto começa com uma letra ou caractere.
print(texto.startswith ("text"))
#verificar se o meu texto termina com uma letra ou caractere
print(texto.endswith("!"))

#para saber se uma varivel contem um determinado carctere
print(texto.count("m")) #quantas vezes determinado caractere ou palavra aparece na varivel.

#teste logico
print("em" in texto)

#substituir algo dentro do texto
print(texto.replace("AINDA", "com certeza"))
#porém entretanto todavia a varivel original não é modificada. 
print(texto)

