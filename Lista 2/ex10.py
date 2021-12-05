vetor1 = input("Digite os 10 elementos separados por vírgula:").split(",")
vetor2 = input("Digite os 10 elementos separados por vírgula:").split(",")
vetor3 = []

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("Vetor com os valores intercalados:", vetor3)