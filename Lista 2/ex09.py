numeros = [int(x) for x in input("Digite os números inteiros separados por vírgula:").split(",")]

soma = 0
for n in numeros:
    soma += n**2

print("A soma dos quadrados dos números é:", soma)