numeros = [int(x) for x in input("Digite os 5 números inteiros separados por vírgula:").split(",")]

soma = numeros[0]
mult = numeros[0]

for n in range(1, len(numeros)):
    soma += numeros[n]
    mult = mult * numeros[n]

print("Números:", numeros)
print("Soma:", soma)
print("Multiplicação:", mult)