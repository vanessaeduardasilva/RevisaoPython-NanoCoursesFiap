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

    return formato_texto


def agenda_para_texto(**agenda_completa):
    """Recebe um dicionario de dicionarios com a agenda que será exibida e 
    retorna uma string com este dicionario formatado"""  

    formato_texto = ""

    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto}\n{contato_para_texto(nome_contato, **formas_contato)}\n"

    return formato_texto


#função para alterar o nome de um contato
def altera_nome_contato(agenda_original:dict, nome_original:str, nome_atualizado:str):
    """Recebe a agenda original em forma de dicionario, o nome_original e o
    nome_atualizado em forma de string.
    Busca o nome original no dicionario e retorna False se não encontrar. 
    Retorna True se encontrar o nome original no dicionario e fizer a exclusão 
    do contato antigo e inclusão do novo"""
    
    if nome_original in agenda_original.keys():
        copia_contratos = agenda_original[nome_original].copy()
        agenda_original.pop(nome_original)
        agenda_original[nome_atualizado] = copia_contratos
        return True
    return False


altera_nome_contato(agenda, "Pessoa 2", "Super Pessoa")
print(agenda_para_texto(**agenda))

#funçao para alterar a forma de contato de alguem 
def altera_forma_contato (lista_contatos:list, valor_antigo:str, novo_valor:str):
    """"Recebe uma lista lista_contatos, o valor antigo que será substituido e o novo valor
    Caso o valor antigo não esteja na lista, retoenará False.
    Caso o valor antigo esteja na lista, será removido, o novo valor será incluido e retornará True."""

    if valor_antigo in lista_contatos:
        posicao_valor_antigo = lista_contatos.index(valor_antigo)
        lista_contatos.pop(posicao_valor_antigo)
        lista_contatos.insert(posicao_valor_antigo, novo_valor)
        return True
    return False