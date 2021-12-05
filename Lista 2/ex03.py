vetor = [float(x) for x in input("Digite as notas separadas por vírgula:").split(",")]

soma = 0
for i in vetor:
    soma += i

print(f"Notas: {vetor[0]}", end='')
for nota in range(1, len(vetor)):
    print(",", vetor[nota], end='')
print()
print("Média:", soma/len(vetor))