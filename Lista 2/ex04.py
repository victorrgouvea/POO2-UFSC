vetor = input("Digite as letras separadas por vírgula:").split(",")
consoantes = []
n_consoantes = 0

for i in vetor:
    if i.lower() not in "aeiou":
        consoantes.append(i)
        n_consoantes += 1

print(f"A lista possue {n_consoantes} consoantes e elas são:", end='')
for c in consoantes:
    print(f' {c}', end='')
print()