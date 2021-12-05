import random

dic = {}

for i in range(10):
    fset = frozenset(random.sample(range(100), 30))
    soma = 0
    for numero in fset:
        soma += numero
    dic[fset] = soma

# Print do dicionário:
for key in list(dic.keys()): 
    print(key, ":", dic[key])