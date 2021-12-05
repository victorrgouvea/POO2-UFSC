dic = {}

for i in range(6):
    nome = input("Digite o nome do corredor:")

    tempos = [float(x) for x in input("Digite os tempos da 10 voltas separados por um espaço em branco:").split()]
    dic[nome] = tempos

fastest_nome = ""
fastest_lap = -1
fastest_index = 0
media_tempos = {}
for key in list(dic.keys()): 
    soma = 0
    for lap in dic[key]:
        if fastest_lap == -1:
            fastest_lap = lap
            fastest_nome = key
            fastest_index = dic[key].index(lap) + 1
        elif lap < fastest_lap:
            fastest_lap = lap
            fastest_nome = key
            fastest_index = dic[key].index(lap) + 1
        soma += lap
    media_tempos[key] = soma/len(dic[key])

count = 1
print("Classificação final:")
while media_tempos != {}:
    menor = min(media_tempos, key=media_tempos.get)
    print(f"{count} - {menor}")
    del media_tempos[menor]
    count += 1

print()
print(f"A melhor volta da prova foi a volta {fastest_index} do piloto {fastest_nome}, com um tempo de {fastest_lap} segundos")
