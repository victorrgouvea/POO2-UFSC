agenda = {}

def incluir_novo_nome(nome: str, telefones: list):
    agenda[nome] = telefones

def incluir_telefone(nome: str, telefone: str):
    if nome not in agenda:
        pergunta = input("Esse nome/telefone não existe na agenda. Deseja acrescentá-lo?")
        if pergunta.lower() == "sim":
            incluir_novo_nome(nome, [telefone])
    else:
        agenda[nome].append(telefone)

def excluir_telefone(nome: str, telefone: str):
    if len(agenda[nome]) == 1:
        del agenda[nome]
    else:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
        else:
            print("Esse telefone não está associado a este nome na agenda")

def excluir_nome(nome: str):
    if nome in agenda:
        del agenda[nome]
    else:
        print("Esse nome não existe na agenda")

def consultar_telefone(nome: str):
    if nome in agenda:
        print(f"Telefones de {nome}:")
        for fone in agenda[nome]:
            print("-", fone)
    else:
        print("Esse nome não existe na agenda")

# Exemplo:
incluir_novo_nome("Alberto Santana", ["991563904", "999281476"])
consultar_telefone("Alberto Santana")
excluir_telefone("Alberto Santana", "991563904")
consultar_telefone("Alberto Santana")
incluir_telefone("Alberto Santana", "991563904")
consultar_telefone("Alberto Santana")
excluir_nome("Alberto Santana")
consultar_telefone("Alberto Santana")
incluir_telefone("Sérgio Noronha", "991432905")
consultar_telefone("Sérgio Noronha")