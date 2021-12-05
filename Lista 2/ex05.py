numeros = [int(x) for x in input("Digite os números inteiros separados por vírgula:").split(",")]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)