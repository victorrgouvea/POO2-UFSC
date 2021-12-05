import string

dic = {} 

def count_palavra(arquivo):
    texto = open(arquivo, "r")  
    for linha in texto: 
        linha = linha.strip() 
        linha = linha.lower() 
        linha = linha.translate(linha.maketrans("", "", string.punctuation)) 
        palavras = linha.split(" ") 
    
        for palavra in palavras: 
            if palavra in dic: 
                dic[palavra] += 1
            else: 
                dic[palavra] = 1

# Exemplo:
count_palavra("texto.txt")

for key in list(dic.keys()): 
    print(key, ":", dic[key])

'''
Outra forma:

from collections import Counter

with open('texto.txt') as f:
    ocorrencias = Counter(f.read().split())
print(ocorrencias) # num de vezes que as palavras aparecem
'''