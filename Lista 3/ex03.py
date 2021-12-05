def media_aluno(nome: str):
    nome = nome.lower()
    notas = dic[nome]
    media = (notas[0] + notas[1]) / 2
    return media

dic = {}

while True:
    nome = input("Digite o nome do aluno:").lower()
    if nome == '':
        break

    notas = [float(x) for x in input("Digite as duas notas do aluno separadas por um espaço em branco:").split()]
    dic[nome] = notas

print(media_aluno("Bruno"))