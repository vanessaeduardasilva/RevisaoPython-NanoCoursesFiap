#tupla que contém contatos suportados pelo sistema 
contatos_suportados = ("telefone", "email", "endereco")

#dicionarios de exemplo, com alguns dados padrão
agenda = {
    "Pessoa 1":{
        "telefone":["11 1234-5678"],
        "e-mail":["pessoa@email.com","pessoa@profissional.com"],
        "endereco":["Rua 123"]
    },

    "Pessoa 2":{
        "telefone":["11 1785-5678"],
        "e-mail":["pessoa2@email.com","pessoa2@profissional.com"],
        "endereco":["Rua 345"]
    }
}

def contato_para_texto(nome_contato:str, **formas_contato):
    """Recebe um nome de contato com string e um dicionario com as formas de contato.
    Retorna uma string com os dados recebidos"""

    formato_texto = f"{nome_contato}"

    for meio_contato, contato in formas_contato.items():
        formato_texto = f"{formato_texto}\n{meio_contato.upper()}"
        contador_formas = 1

        for valor in contato:
            formato_texto = f"{formato_texto}\n\t{contador_formas} - {valor.upper()}"
            contador_formas += 1

def agenda_para_texto(**agenda_completa):
    """Recebe um dicionario de dicionarios com a agenda que será exibida e 
    retorna uma string com este dicionario formatado"""  
    formato_texto = ""
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto}------------\n"              

    return formato_texto


print(agenda_para_texto(**agenda))