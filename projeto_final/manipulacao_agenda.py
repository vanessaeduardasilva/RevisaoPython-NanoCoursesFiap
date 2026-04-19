import json


contatos_suportados = ("telefone", "email", "endereço")

agenda = {
    "Pessoa 1":{
        "telefone":["11 1234-5678"],
        "email":["pessoa@email.com", "email@profissional.com"],
        "endereco":["Rua 123"]
    },
    "Pessoa 2":{
        "telefone":["11 9874-5678"],
        "email":["pessoa2@email.com", "pessoa2@profissional.com"],
        "endereco":["Rua 345"]
    }
}

def agenda_para_txt(nome_arquivo:str, agenda):
    if "txt" not in nome_arquivo:
        nome_arquivo = f"{nome_arquivo}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(agenda_para_texto(**agenda))
        print("Agenda exportada com sucesso!")

def json_para_agenda(nome_arquivo:str):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print("Agenda carregada com sucesso!")
    return json.loads(conteudo)

def agenda_para_json(nome_arquivo:str, agenda):
    if ".json" not in nome_arquivo:
        nome_arquivo = f"{nome_arquivo}.json"
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(json.dumps(agenda, indent=4, ensure_ascii=False))
            print("Agenda exportada com sucesso!")
    

def contato_para_texto(nome_contato:str, **formas_contato):
    """Recebe um nome de contato com string e um dicionário
     com as formas de contato.
     Retorna uma string com os dados recebidos"""
    formato_texto = f"{nome_contato}"
    for meio_contato, contato in formas_contato.items():
        formato_texto = f"{formato_texto}\n{meio_contato.upper()}"
        contador_formas = 1
        for valor in contato:
            formato_texto = f"{formato_texto}\n\t{contador_formas} - {valor.upper()}"
            contador_formas = contador_formas + 1

    return formato_texto

def agenda_para_texto(**agenda_completa):
    """Recebe um dicionário de dicionários com a agenda que será exibida e 
    retorna uma string com este dicionário formatado"""
    formato_texto = ""
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto}{contato_para_texto(nome_contato, **formas_contato)}\n"
        formato_texto = f"{formato_texto}---------------------------\n"
    return formato_texto


def altera_nome_contato(agenda_original:dict, nome_original:str, nome_atualizado:str):
    """Recebe a agenda original em forma de dicionário, o nome_original e o nome_atualizado em forma
    de string. 
    Busca o nome original no dicionário e retorna False se não encontrar.
    Retorna True se encontrar o nome original no dicionário e fizer a exclusão do contato antigo e inclusão do novo"""
    if nome_original in agenda_original.keys():
        copia_contatos = agenda_original[nome_original].copy()
        agenda_original.pop(nome_original)
        agenda_original[nome_atualizado] = copia_contatos
        return True
    return False


def altera_forma_contato(lista_contatos:list, valor_antigo:str, novo_valor:str):
    """Recebe uma list lista_contatos, o valor antigo que será substituído e o novo valor
    Caso o valor antigo não esteja na lista, retornará False.
    Caso o valor antigo esteja na lista, será removido, o novo valor será incluido e retornará True
    """
    if valor_antigo in lista_contatos:
        posicao_valor_antigo = lista_contatos.index(valor_antigo)
        lista_contatos.pop(posicao_valor_antigo)
        lista_contatos.insert(posicao_valor_antigo, novo_valor)
        return True
    return False

def exclui_contato(agenda:dict, nome_contato:str):
    """Recebe uma agenda completa como dicionário e o nome do contato como string.
    Caso o nome do contato não esteja nas chaves do dicionário, retornará False
    Caso o nome do contato esteja nas chaves, o registro correspondente será removido e retornará True"""
    if nome_contato in agenda.keys():
        agenda.pop(nome_contato)
        return True
    return False

def inclui_contato(agenda:dict, nome_contato:str, **formas_contato):
    """Recebe uma agenda completa como dicionário, o nome do novo contato como string e as formas de contato
    em um dicionário como **kwargs.
    Não é feita nenhuma verifição, portanto se já existir um contato com o mesmo nome, será sobrescrito"""
    #print(formas_contato)
    agenda[nome_contato] = formas_contato

def inclui_forma_contato(formas_contato:dict, forma_incluida:str, valor_incluido:str):
    """Recebe um dicionário com as formas de contato, a forma de contato que será incluida ou 
    alterada e o valor que será incluído.
    Caso a forma de contato já possua valores, o novo valor será adicionado na lista e retornará True.
    Caso a forma de contato ainda não exista e estiver presente na tupla de formas de contatos suportados
     será incluída e o novo valor será incluído em uma lista, retornando True.
     Caso a forma de contato ainda não exista e não estiver presente na tupla de formas de contato suportados,
     retornará False"""
    if forma_incluida in formas_contato.keys():
        formas_contato[forma_incluida].append(valor_incluido)
        return True
    elif forma_incluida in contatos_suportados:
        formas_contato[forma_incluida] = [valor_incluido]
        return True
    return False

def usuario_inclui_contato(agenda:dict):
    nome = input("Informe o nome do novo contato que será inserido na agenda: ")
    dicionario_formas = {}
    for forma in contatos_suportados:
        resposta = input(f"Deseja inserir um {forma} para {nome.upper()}? \nSIM ou NÃO -> ")
        lista_contatos = []
        while "S" in resposta.upper():
            lista_contatos.append(input(f"Informe um {forma}: "))
            resposta = input(f"Deseja inserir outro {forma} para {nome.upper()}?\nSIM ou NÃO -> ")
        if len(lista_contatos) > 0:
            dicionario_formas[forma] = lista_contatos.copy()
            lista_contatos.clear()
    if len(dicionario_formas.keys()) > 0:
        inclui_contato(agenda, nome, **dicionario_formas)
        print("Inclusão bem sucedida!")
    else:
        print("É necessário incluir pelo menos uma forma de contato!\nA agenda não foi alterada.")

def usuario_inclui_forma_contato(agenda:dict):
    #inclui_forma_contato(formas_contato:dict, forma_incluida:str, valor_incluido:str):
    nome = input("Informe o nome do contato para o qual deseja incluir formas de contato ")
    if nome in agenda.keys():
        print(f"As formas de contato suportadas pelo sistema são: {contatos_suportados}")
        forma_incluida = input("Qual forma de contato deseja incluir? ")
        if forma_incluida in contatos_suportados:
            valor_incluido = input(f"Informe o {forma_incluida} que deseja incluir: ")
            if inclui_forma_contato(agenda[nome], forma_incluida, valor_incluido):
                print("Operação bem sucedida! A nova forma de contato foi incluida! ")
            else:
                print("Ocorreu um erro durante a inserção. A agenda não foi alterada.")
        else:
            print("A forma de contato indicada não é suportada pelo sistema. A agenda não foi alterada.")
    else:
        print("O contato informado não existe na agenda. Não foram feitas alterações. ")

def usuario_exclui_contato(agenda:dict):
    nome = input("Informe o nome do contato que deseja excluir: ")
    if exclui_contato(agenda, nome):
        print("Usuário excluido com sucesso!")
    else:
        print("Nome do usuário não localizado na agenda. Não foram feitas alterações.")

def usuario_altera_forma_contato(agenda:dict):
    nome = input("Informe o nome do contato que deseja alterar: ")
    if nome in agenda.keys():
        print(f"As formas de contato suportadas pelo sistema são: {contatos_suportados}")
        forma_incluida = input("Qual forma de contato deseja incluir? ")
        if forma_incluida in contatos_suportados:
            print(contato_para_texto(nome, **agenda[nome]))
            valor_antigo = input(f"Informe o {forma_incluida} que deseja alterar " )
            nova_valor = input(f"Informe o novo {forma_incluida} ")
            if altera_forma_contato(agenda[nome][forma_incluida], valor_antigo, nova_valor):
                print("Contato alterado com sucesso!")
            else:
                print("Ocorreu um erro durante a alteração do contato. A agenda não foi alterada.")
        else:
            print(f"{forma_incluida} nõa é uma forma de contato suportada pelo sistema. A agenda não foi alterada.")
    else:
        print(f"O contato {nome} não está na agenda. A agenda não foi alterada.")

def usuario_altera_nome_contato(agenda:dict):
    #altera_nome_contato(agenda_original:dict, nome_original:str, nome_atualizado:str):
    nome_original = input("Informe o nome do contato que deseja alterar: ")
    nome_atualizado = input("Informe o nome do novo contato: ")
    if altera_nome_contato(agenda, nome_original, nome_atualizado):
        print(f"O contato foi atualizado e agora se chama {nome_atualizado}")
    else:
        print(f"O contato original não foi localizado. A agenda não foi alterada.")

def usuario_contato_para_texto(agenda:dict):
    nome = input("Informe o nome do contato que deseja exibir: ")
    if nome in agenda.keys():
        print(contato_para_texto(nome, **agenda[nome]))
    else:
        print("O contato informado não está na agenda.")


def exibe_menu():
    print("\n\n")
    print("1 - Incluir contato na agenda")
    print("2 - Incluir uma forma de contato")
    print("3 - Alterar o nome de um contato")
    print("4 - Alterar uma forma de contato")
    print("5 - Exibir um contato")
    print("6 - Exibir toda a agenda")
    print("7 - Excluir um contato")
    print("8 - Exportar agenda para txt")
    print("9 - Exportar agenda para JSON")
    print("10 - Importar agenda de JSON")
    print("11 - Sair")
    print("\n")

def manipulador_agenda():
    agenda = {}
    op = 1
    while op != 11:
        exibe_menu()
        op = int(input("Informe a opção desejada: "))
        if op == 1:
            usuario_inclui_contato(agenda)
        elif op == 2:
            usuario_inclui_forma_contato(agenda)
        elif op == 3:
            usuario_altera_nome_contato(agenda)
        elif op == 4:
            usuario_altera_forma_contato(agenda)
        elif op == 5:
            usuario_contato_para_texto(agenda)
        elif op == 6:
            print(agenda_para_texto(**agenda))
        elif op == 7:
            usuario_exclui_contato(agenda)
        elif op == 8:
            nome_arquivo = input("Informe o nome ou caminho do arquivo: ")
            agenda_para_txt(nome_arquivo, agenda)
        elif op == 9:
            nome_arquivo = input("Informe o nome ou caminho do arquivo: ")
            agenda_para_json(nome_arquivo, agenda)
        elif op == 10:
            nome_arquivo = input("Informe o nome ou caminho do arquivo: ")
            agenda = json_para_agenda(nome_arquivo)
        elif op == 11:
            print("Saindo do sistema")
            break
        else:
            print("Opção inválida! Informe uma opção existente.")


manipulador_agenda()