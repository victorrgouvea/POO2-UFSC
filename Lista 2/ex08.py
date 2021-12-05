idades = []
alturas = []
for i in range(5):
    infos = input("Digite a idade e a altura, respectivamente, separados por vírgula:").split(",")
    idades.append(infos[0])
    alturas.append(infos[1])

for i in range(4, -1, -1):
    print(f"Idade: {idades[i]} / Altura: {alturas[i]}")